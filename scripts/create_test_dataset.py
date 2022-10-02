import os
import click
import shutil as sh
from pathlib import Path
from glob import glob


@click.command()
@click.argument("input_path", type=click.Path(exists=True))
def create_test_dataset(input_path: str):
    """
    Create test dataset from validation dataset
    :param input_path: path with input data
    """
    ann_dir = input_path + "/" + f"labels/test" + "/"
    img_dir = input_path + "/" + f"images/test" + "/"

    Path.mkdir(Path(ann_dir), parents=True, exist_ok=True)
    Path.mkdir(Path(img_dir), parents=True, exist_ok=True)
    
    all_images_paths = [
            path
            for path in glob(
                f"{input_path}/images/val/*"
            )
    ]

    for name in all_images_paths[-261:]:
        filename = os.path.basename(name)
        sh.move(f"{input_path}/images/val/{filename}", f"{img_dir}{filename}")
        annotation_name = ".".join(filename.split('.')[:-1]) + ".txt"
        sh.move(f"{input_path}/labels/val/{annotation_name}", f"{ann_dir}{annotation_name}")
        


if __name__ == "__main__":
    create_test_dataset()
