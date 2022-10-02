import yaml
import click
import shutil as sh
from pathlib import Path
from glob import glob


@click.command()
@click.argument("input_path", type=click.Path(exists=True))
@click.argument("output_path", type=click.Path())
def create_config(input_path: str, output_path: str):
    """
    Create yolo config
    :param input_path: path with data
    :param input_path: path to config
    """
    custom_config = {"train": f"./../{input_path}/train.txt",
                "val": f"./../{input_path}/val.txt",
                "test": f"./../{input_path}/test.txt",
                "nc": 1,
                "names": ['number']}
                 
    with open(output_path, 'w') as file:
        yaml.dump(custom_config, file)

        


if __name__ == "__main__":
    create_config()
