import unittest

from aiml_template import SampleClass


class ValidityTest(unittest.TestCase):
    def setUp(self):
        self.model = SampleClass()

    def tearDown(self):
        pass

    def test_validity(self):
        assert_criteria = True

        assert assert_criteria
