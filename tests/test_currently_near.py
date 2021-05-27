import unittest

from populace import currently_near

class TestCurrentlyNear(unittest.TestCase):

    def test_valid_city_with_results(self):
        """
        Test method returns correct number of users for a valid city
        """
        users = currently_near("London")
        self.assertEqual(len(users), 3)

    def test_valid_city_with_no_results(self):
        """
        Test method returns no users for a valid city with noone nearby
        """
        users = currently_near("Newcastle")
        self.assertEqual(len(users), 0)

    def test_invalid_city(self):
        """
        Test method returns no users for an invalid city
        """
        users = currently_near("foo")
        self.assertEqual(len(users), 0)

    def test_valid_city_with_bigger_radius(self):
        """
        Test method returns more users if radius is increased
        """
        users = currently_near("London", radius=150)
        self.assertEqual(len(users), 7)

    def test_valid_city_with_smaller_radius(self):
        """
        Test method returns more users if radius is increased
        """
        users = currently_near("London", radius=25)
        self.assertEqual(len(users), 2)

    def test_invalid_radius(self):
        """
        Test method throws an error if invalid radius is supplied
        """
        with self.assertRaises(TypeError):
            currently_near("London", radius="bar")
