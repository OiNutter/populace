import unittest
import requests

from populace import _query

class TestQuery(unittest.TestCase):

    def test_valid_endpoint(self):
        """
        Test method returns valid json
        """
        response = _query("https://dwp-techtest.herokuapp.com/swagger.json")
        self.assertIs(type(response), dict)

    def test_invalid_endpoint_raises_exception(self):
        """
        Test invalid url raises exception
        """
        with self.assertRaises(requests.exceptions.RequestException):
            response = _query("foo")

    def test_bad_response_raises_exception(self):
        """
        Test bad response raises an exception
        """
        with self.assertRaises(requests.exceptions.HTTPError):
            response = _query("https://dwp-techtest.herokuapp.com/city")
