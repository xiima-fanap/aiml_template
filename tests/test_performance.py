import unittest

from aiml_template import SampleClass


class PerformanceTest(unittest.TestCase):
    def setUp(self):
        self.model = SampleClass()

    def tearDown(self):
        pass

    def test_performance(self):
        assert_criteria = True

        assert assert_criteria
