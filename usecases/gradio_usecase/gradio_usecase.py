"""Visualize aiml_template using Gradio WebUI"""

import gradio

from aiml_template import SampleClassVisualize


def _load_model():
    """Load SampleClassVisualize model"""

    sample_class = SampleClassVisualize()

    return sample_class


def _process(image):
    """Apply SampleClassVisualize on uploaded image"""

    _, image_visualized = sample_class_visualize.sample_method_visualize(
        image
    )

    return image_visualized


def _create_input():
    """Instanciate image input for Gradio UI"""

    input_image = gradio.inputs.Image(
        shape=None,
        image_mode="RGB",
        invert_colors=False,
        source="upload",
        tool="editor",
        type="numpy",
        label="Image to be processed",
        optional=False
    )

    return input_image


def _create_output():
    """Instanciate image output for Gradio UI"""

    output_image = gradio.outputs.Image(
        type="auto", label="Model output"
    )

    return output_image


def _launch(input_image, output_image):
    """Launch Gradio UI on localhost"""

    iface = gradio.Interface(
        fn=_process,
        inputs=input_image,
        outputs=output_image,
    )
    iface.launch(server_name="0.0.0.0")


if __name__ == "__main__":
    sample_class_visualize = _load_model()

    input_image = _create_input()
    output_image = _create_output()

    _launch(input_image, output_image)
