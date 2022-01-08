"""Apply aiml_sample on a directory of images and visualize the response. Store
the visualized images in the output directory.
"""

import os
import cv2
import yaml
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


def _list_image_paths(configs):
    """List all image input-output path pairs"""

    image_paths = []

    input_directory = configs["input_images_directory"]
    output_directory = configs["output_images_directory"]

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    image_names = os.listdir(input_directory)
    for image_name in image_names:
        input_image_path = os.path.join(
            configs["input_images_directory"],
            image_name
        )

        output_image_path = os.path.join(
            configs["output_images_directory"],
            image_name
        )

        image_paths.append(
            {
                "read_from": input_image_path,
                "write_to": output_image_path
            }
        )

    return image_paths


def _run_test(configs):
    """Load model and process all images"""

    model = SampleClassVisualize()

    read_write_map = _list_image_paths(configs)
    for read_write_paths in tqdm(read_write_map):
        image = cv2.imread(read_write_paths["read_from"])
        
        _, image_visualized = model.sample_method_visualize(image)

        image_resized = cv2.resize(image_visualized, (1280, 720))
        cv2.imwrite(read_write_paths["write_to"], image_resized)


if __name__ == "__main__":
    args = _read_arguments()
    configs = _read_configs(args.config_path)

    _run_test(configs)
