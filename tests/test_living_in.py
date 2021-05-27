import unittest

from populace import living_in

class TestLivingIn(unittest.TestCase):

    def test_valid_city_with_results(self):
        """
        Test method returns correct number of users for a valid city
        """
        users = living_in("London")
        self.assertEqual(len(users), 6)

    def test_valid_city_with_no_results(self):
        """
        Test method returns no users for a valid empty city
        """
        users = living_in("Newcastle")
        self.assertEqual(len(users), 0)

    def test_invalid_city(self):
        """
        Test method returns no users for an invalid city
        """
        users = living_in("foo")
        self.assertEqual(len(users), 0)
