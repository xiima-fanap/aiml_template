"""An example usage of the implemented module

Example should be a bare-minimum application of the module with all unncessary
details removed.
The aim is to show a new user how to start using the module in the fastest way.
"""

import cv2

from aiml_template import SampleClass
from aiml_template import SampleClassVisualize


def example_sample_class():
    image = cv2.imread("./example.png")

    sample_class = SampleClass()
    response = sample_class.sample_method(image)

    print("Response: {}".format(response))


def example_sample_class_visualize():
    image = cv2.imread("./example.png")

    sample_class = SampleClassVisualize()
    response, image_visualized = sample_class.sample_method_visualize(image)

    print("Image: {} Response: {}".format(
            image_visualized.shape, response
        )
    )


def example_print():
    print("This is an example")


if __name__ == "__main__":
    print("Running examples\n{}".format('-' * 20))

    for key in list(locals()):
        if callable(locals()[key]) and "example" in key:
            print("Running '{}'...\n".format(key))
            locals()[key]()
            print("{}".format('-' * 20))
    
    print("Done running examples.")
