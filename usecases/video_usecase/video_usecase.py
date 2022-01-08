"""Apply aiml_sample on a directory of videos and visualize the response. Store
the visualized videos in the output directory.
"""

import os
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


def _list_video_paths(configs):
    """List all video input-output path pairs"""

    video_paths = []

    input_directory = configs["input_videos_directory"]
    output_directory = configs["output_videos_directory"]

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    video_names = os.listdir(input_directory)
    for video_name in video_names:
        input_video_path = os.path.join(
            configs["input_videos_directory"],
            video_name
        )

        output_video_path = os.path.join(
            configs["output_videos_directory"],
            video_name
        )

        video_paths.append(
            {
                "read_from": input_video_path,
                "write_to": output_video_path
            }
        )

    return video_paths


def _run_test(configs):
    """Load model and process all videos"""

    model = SampleClassVisualize()

    read_write_map = _list_video_paths(configs)
    for read_write_paths in tqdm(read_write_map):
        # Process, visualize, and write the video
        pass


if __name__ == "__main__":
    args = _read_arguments()
    configs = _read_configs(args.config_path)

    _run_test(configs)
