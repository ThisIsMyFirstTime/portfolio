from unittest import TestCase
from functions import divide


class TestFunctions(TestCase):
    def test_divide_result(self):
        dividend = 15
        divisor = 3
        expected_result = 5.0
        self.assertEqual(divide(dividend, divisor), expected_result)
        