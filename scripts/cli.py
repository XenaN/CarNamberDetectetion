import click

from api import create_annotations
from api import create_config
from api import create_list_files
from api import create_test_dataset


@click.group()
def cli():
    pass


@click.command()
@click.option("--input", "inp", type=click.Path(exists=True))
@click.option("--output", type=click.Path())
def ann(inp, output):
    """Create annotation with class and box edges in txt format"""
    create_annotations(inp, output)


@click.command()
@click.option("--input", "inp", type=click.Path(exists=True))
@click.option("--output", type=click.Path())
def conf(inp, output):
    """Create yolo config"""
    create_config(inp, output)


@click.command()
@click.option("--input", "inp", type=click.Path(exists=True))
def lists(inp):
    """Create lists with filenames for yolo"""
    create_list_files(inp)


@click.command()
@click.option("--input", "inp", type=click.Path(exists=True))
def dataset(inp):
    """Create test dataset from validation dataset"""
    create_test_dataset(inp)


cli.add_command(ann)
cli.add_command(conf)
cli.add_command(lists)
cli.add_command(dataset)


if __name__ == "__main__":
    cli()
