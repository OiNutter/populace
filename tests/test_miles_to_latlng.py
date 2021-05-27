import unittest
import requests

from populace import _change_in_latitude, _change_in_longitude

class TestMilesToLatLng(unittest.TestCase):

    def test_change_in_latitude(self):
        """
        Test method correct latitude adjustment
        """
        result = _change_in_latitude(100)
        self.assertEqual(result, 1.4468631190172303)

    def test_change_in_longitude(self):
        """
        Test method returns correct longitude adjustment
        """
        result = _change_in_longitude(10,100)
        self.assertEqual(result, 1.4691833148061078)

    def test_throws_exception_if_invalid_argument(self):
        """
        Test methods throw TypeErrors if non numeric arguments passed
        """
        with self.assertRaises(TypeError):
            _change_in_latitude("bob")

        with self.assertRaises(TypeError):
            _change_in_longitude("ted", 100)

        with self.assertRaises(TypeError):
            _change_in_longitude(10, "alice")
