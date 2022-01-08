"""Apply aiml_sample on a HDF5 dataset of images and calculate the model
accuracy.
"""

import yaml
import h5py
import argparse

from tqdm import tqdm
from aiml_template import SampleClassVisualize


def _read_arguments():
    """Create CLI interface and read the arguments"""

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-c', '--config_path',
        help=(
            "Path to the config file"
        ),
        type=str,
        required=True
    )

    return parser.parse_args()


def _read_configs(config_path):
    """Load configs as a dict from a YAML file"""

    configs = None
    with open(config_path, 'r') as yaml_file:
        configs = yaml.safe_load(yaml_file)

    return configs


def _run_test(configs):
    pass


if __name__ == "__main__":
    args = _read_arguments()
    configs = _read_configs(args.config_path)

    _run_test(configs)
