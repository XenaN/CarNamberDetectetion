import json
from pathlib import Path
import platform
import shutil
from typing import Dict

import imagesize
from tqdm import tqdm
import yaml

from utils.types import PathLike


def calculate_coco_type_box(
    shape: Dict, image_width: int, image_height: int
) -> str:
    """
    Recalculate box edges

    Args:
        shape: shape of box
        image_width: width of image
        image_height: height of image

    Returns:
        Recalculated box-string

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


def create_annotations(input_path: PathLike, output_path: PathLike):
    """
    Create annotation with class and box edges in txt

    Args:
        input_path: path with input data
        output_path: path to output data

    """

    input_path = Path(input_path).resolve()
    output_path = Path(output_path).resolve()

    for subset in ["train", "val"]:
        annotations_path = next(input_path.rglob(f"{subset}/*.json"))

        with open(annotations_path, "r", encoding="utf-8") as f:
            annotation = json.loads(f.read())

        ann_dir = output_path / f"labels/{subset}"
        img_dir = output_path / f"images/{subset}"

        Path.mkdir(Path(ann_dir), parents=True, exist_ok=True)
        Path.mkdir(Path(img_dir), parents=True, exist_ok=True)

        region_numbers = [
            (fn["filename"], fn["regions"])
            for fn in list(annotation["_via_img_metadata"].values())
        ]

        for filename, regions in tqdm(region_numbers):

            original = input_path / subset / filename
            copied_tmp_link = img_dir / "filename.tmp"
            copied = img_dir / filename

            if platform.system() not in ("Linux", "Darwin"):
                shutil.copy(original, copied)
            else:
                copied_tmp_link.symlink_to(original)
                copied_tmp_link.rename(copied)

            image_width, image_height = imagesize.get(original)

            buff = []

            for shape_attrs in filter(
                lambda x: x["name"] == "polygon",
                (region["shape_attributes"] for region in regions),
            ):
                box = calculate_coco_type_box(
                    shape_attrs, image_width, image_height
                )
                buff.append(box)

            ann_content = "".join(buff)
            basename = ".".join(filename.split(".")[:-1])
            txt_save_path = ann_dir / f"{basename}.txt"

            with open(txt_save_path, "w") as f:
                f.write(ann_content)


def create_config(input_path: PathLike, output_path: PathLike):
    """
    Create yolo config

    Args:
        input_path: path with input data
        output_path: path to output data
    """

    input_path = Path(input_path).resolve()
    output_path = Path(output_path).resolve()

    train = input_path / "train.txt"
    val = input_path / "val.txt"
    test = input_path / "test.txt"

    custom_config = {
        "train": f"{train!s}",
        "val": f"{val!s}",
        "test": f"{test!s}",
        "nc": 1,
        "names": ["number"],
    }

    with open(output_path, "w") as file:
        yaml.dump(custom_config, file)


def create_list_files(input_path: PathLike):
    """
    Create lists with filenames for yolo

    Args:
        input_path: path with input data
    """

    input_path = Path(input_path).resolve()

    for subset in ["train", "val", "test"]:

        all_images_paths = [
            path.resolve()
            for path in input_path.joinpath("images", subset).rglob(
                "*"
            )
        ]

        with open(f"{input_path}/{subset}.txt", "w") as f:
            for path in all_images_paths:
                f.write(f"{path}\n")


def create_test_dataset(input_path: PathLike):
    """
    Create test dataset from validation dataset

    Args:
        input_path: path with input data

    """

    input_path = Path(input_path).resolve()

    ann_dir = input_path / "labels" / "test"
    img_dir = input_path / "images" / "test"

    Path.mkdir(Path(ann_dir), parents=True, exist_ok=True)
    Path.mkdir(Path(img_dir), parents=True, exist_ok=True)

    all_images_paths = [
        path
        for path in input_path.joinpath("images", "val").rglob("*")
    ]

    for name in all_images_paths[-261:]:
        filename = name.name

        shutil.move(
            input_path / "images" / "val" / filename,
            img_dir / filename,
        )

        annotation_name = (
            ".".join(str(filename).split(".")[:-1]) + ".txt"
        )

        shutil.move(
            input_path / "labels" / "val" / annotation_name,
            ann_dir / annotation_name,
        )


def create_config_yolov5(input_path: PathLike, output_path: PathLike):
    """
    Create yolo config

    Args:
        input_path: path with input data
        output_path: path to output data
    """

    input_path = Path(input_path).resolve()
    output_path = Path(output_path).resolve()

    train = "train.txt"
    val = "val.txt"
    test = "test.txt"

    custom_config = {
        "path": f"{input_path!s}",
        "train": f"{train!s}",
        "val": f"{val!s}",
        "test": f"{test!s}",
        "names": {0: "number"},
    }

    with open(output_path, "w") as file:
        yaml.dump(custom_config, file)
