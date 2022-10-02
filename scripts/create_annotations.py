import os.path
from typing import Dict
import json
import click
import imagesize
import shutil as sh
from pathlib import Path
from glob import glob
from tqdm import tqdm


def calculate_coco_type_box(shape: Dict, image_width: int, image_height: int):
    """
    Recalculate box edges
    :param shape: key from annotation dictionary
    :param image_width: image width
    :param image_height: image height
    """
    all_points_x = shape["all_points_x"]
    all_points_y = shape["all_points_y"]
    width = (max(all_points_x) - min(all_points_x)) / image_width
    height = (max(all_points_y) - min(all_points_y)) / image_height

    x_center = min(all_points_x) / image_width + width / 2
    y_center = min(all_points_y) / image_height + height / 2
    
    annotation_box = "0 {:.6f} {:.6f} {:.6f} {:.6f}\n".format(
                        x_center, y_center, width, height
                    )
    return annotation_box


@click.command()
@click.argument("input_path", type=click.Path(exists=True))
@click.argument("output_path", type=click.Path())
def create_correct_annotations(input_path: str, output_path: str):
    """
    Create annotaion with class and box edges in txt
    :param input_path: path with input data
    :param output_path: path to save file
    """
    for subset in ["train", "val"]:
        all_images_paths = [
            path
            for path in glob(
                f"{input_path}/{subset}/*"
            )
            if ".json" not in path and ".sh" not in path
        ]
        annotations_path = [
            path
            for path in glob(
                f"{input_path}/{subset}/*"
            )
            if ".json" in path
        ][0]
    
        with open(annotations_path, "r", encoding='utf-8') as f:
            annotation = json.loads(f.read())

        ann_dir = output_path + "/" + f"labels/{subset}" + "/"
        img_dir = output_path + "/" + f"images/{subset}" + "/"

        Path.mkdir(Path(ann_dir), parents=True, exist_ok=True)
        Path.mkdir(Path(img_dir), parents=True, exist_ok=True)

        region_numbers = [
            (fn["filename"], fn["regions"])
            for fn in list(annotation["_via_img_metadata"].values())
        ]

        for filename, regions in tqdm(region_numbers):

            original = input_path + "/" + subset + "/" + filename
            copied = img_dir + filename

            sh.copy(original, copied)

            image_width, image_height = imagesize.get(original)
            ann_content = ""
            for region in regions:
                shape_attributes = region["shape_attributes"]
                if shape_attributes["name"] == "polygon":
                    ann_content += calculate_coco_type_box(shape_attributes, image_width, image_height)

            basename = ".".join(filename.split(".")[:-1])
            txt_save_path = ann_dir + basename + ".txt"

            with open(txt_save_path, "w") as f:
                f.write(ann_content)
        


if __name__ == "__main__":
    create_correct_annotations()
