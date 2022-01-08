"""Main module file"""

import numpy as np

from aiml_template import ExceptionInvalidInput


class SampleClass:
    """Sample class to make the aiml template more tangible
    """

    def __init__(self) -> None:
        """Init method"""
        pass

    def sample_method(self, image:np.ndarray) -> str:
        """Sample method to do inference
        
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

        self._assert_type(image, np.ndarray)

        response = self._sample_private_method(image)

        return response

    def _sample_private_method(self, image:np.ndarray) -> str:
        """Sample internal private method for hidden processing"""
        return ""

    @staticmethod
    def _assert_type(image, type_):
        if not isinstance(image, type_):
            raise ExceptionInvalidInput(
                "Required input type is {} but received {}".format(
                    type_, type(input)
                )
            )
