"""An example usage of the implemented module

Example should be a bare-minimum application of the module with all unncessary
details removed.
The aim is to show a new user how to start using the module in the fastest way.
"""

import cv2

from aiml_template import SampleClass
from aiml_template import SampleClassVisualize


def example_sample_class(image :np.ndarray)-> str:
    """Sample method to do a great 
        
        Parameters
        ----------
        image : np.ndarray
            The image to process

        Returns
        -------
        str
            Response in json format

        Raises
        ------
        ExceptionInvalidInput
            If input type is not np.ndarray
     """
    image = cv2.imread(image)

    sample_class = SampleClass()
    response = sample_class.sample_method(image)

     return "{Response: {}}".format(response)

if __name__ == "__main__":
    print("Running examples\n{}".format('-' * 20))

    for key in list(locals()):
        if callable(locals()[key]) and "example" in key:
            print("Running '{}'...\n".format(key))
            locals()[key]()
            print("{}".format('-' * 20))
    
    print("Done running examples.")
