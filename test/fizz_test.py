"""
This is a test file for the Fizz class.
"""
import unittest

from src.fizz import Fizz

class FizzTest(unittest.TestCase):
    """
    This is a test class for the Fizz class.
    """
    def setUp(self):
        self.fizz = Fizz()


    def test_1(self):
        """
        Test the convert method
        """
        self.assertEqual(self.fizz.convert(1), "1")

    def test_2(self):
        """
        Test the convert method
        """
        self.assertEqual(self.fizz.convert(2), "1 2")

    def test_3(self):
        """
        Test the convert method
        """
        self.assertEqual(self.fizz.convert(3), "1 2 Fizz")

    def test_4(self):
        """
        Test the convert method
        """
        self.assertEqual(self.fizz.convert(4), "1 2 Fizz 4")

    def test_15(self):
        """
        Test the convert method
        """
        self.assertEqual(self.fizz.convert(15),
    "1 2 Fizz 4 Buzz Fizz Whizz 8 Fizz Buzz 11 Fizz 13 Whizz FizzBuzz")
