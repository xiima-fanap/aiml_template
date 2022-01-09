"""Composing the SampleClass to make an extend class to visualize the inference
results
"""

import numpy as np

from aiml_template import SampleClass


class SampleClassVisualize:
    """Sample class to visualize inference results

    Methods
    -------
    sample_method_visualize(image:np.ndarray)
        Sample method to do inference and visualize the response
    """

    def __init__(self) -> None:
        """Init method"""
        
        self.sample_class = SampleClass()

    def sample_method_visualize(self, image:np.ndarray) -> \
            tuple((str, np.ndarray)):
        """Sample method to do inference and visualize the response
        
        Parameters
        ----------
        image : np.ndarray
            The image to process

        Returns
        -------
        Tuple(str, np.ndarray)
            A tuple of (response, visualize_image)

        Raises
        ------
        ExceptionInvalidInput
            If input type is not np.ndarray
        """

        response = self.sample_class.sample_method(image)
        image_visualized = self._sample_private_method_visualize(response)

        return response, image_visualized

    def _sample_private_method_visualize(self, result:str) -> np.ndarray:
        """Sample internal private method for hidden processing"""
        
        return np.empty((1))
