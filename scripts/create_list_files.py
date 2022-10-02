import os
import click
import shutil as sh
from pathlib import Path
from glob import glob


@click.command()
@click.argument("input_path", type=click.Path(exists=True))
def create_list_files(input_path: str):
    """
    Create lists with filenames for yolo
    :param input_path: path with input data
    """
    for subset in ["train", "val", "test"]:
        all_images_paths = [
                os.path.abspath(path)
                for path in glob(
                    f"{input_path}images/{subset}/*"
                )
        ]
        
        
        with open(f"{input_path}/{subset}.txt", 'w') as f:
            for path in all_images_paths:
                f.write(f"{path}\n")
        


if __name__ == "__main__":
    create_list_files ()
