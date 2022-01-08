import unittest

from aiml_template import SampleClass


class AccuracyTest(unittest.TestCase):
    def setUp(self):
        self.model = SampleClass()

    def tearDown(self):
        pass

    def test_accuracy(self):
        assert_criteria = True

        assert assert_criteria
