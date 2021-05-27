import unittest
import requests

from populace import _in_bounds

class TestInBounds(unittest.TestCase):

    def test_in_bounds(self):
        """
        Test method returns true for in bound coordinate
        """
        result = _in_bounds(1,1,0,2,0,2)
        self.assertTrue(result)

    def test_out_of_bounds(self):
        """
        Test method returns false for out of bounds coordinate
        """
        result = _in_bounds(3,3,0,2,0,2)
        self.assertFalse(result)

    def test_both_coordinates_in_bounds(self):
        """
        Test method only returns true if both coordinates in bounds
        """
        result = _in_bounds(1,3,0,2,0,2)
        self.assertFalse(result)
        result2 = _in_bounds(3,1,0,2,0,2)
        self.assertFalse(result)
