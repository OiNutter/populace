import unittest

from populace import find_users

class TestFindUsers(unittest.TestCase):

    def test_valid_city_with_results(self):
        """
        Test method returns correct number of users for a valid city
        """
        users = find_users("London")
        self.assertEqual(len(users), 9)

    def test_valid_city_with_no_results(self):
        """
        Test method returns no users for a valid city with noone nearby
        """
        users = find_users("Newcastle")
        self.assertEqual(len(users), 0)

    def test_invalid_city(self):
        """
        Test method returns no users for an invalid city
        """
        users = find_users("foo")
        self.assertEqual(len(users), 0)

    def test_valid_city_with_bigger_radius(self):
        """
        Test method returns more users if radius is increased
        """
        users = find_users("London", radius=150)
        self.assertEqual(len(users), 13)

    def test_valid_city_with_smaller_radius(self):
        """
        Test method returns more users if radius is increased
        """
        users = find_users("London", radius=25)
        self.assertEqual(len(users), 8)

    def test_invalid_radius(self):
        """
        Test method throws an error if invalid radius is supplied
        """
        with self.assertRaises(TypeError):
            find_users("London", radius="bar")
