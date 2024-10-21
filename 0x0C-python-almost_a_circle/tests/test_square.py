#!/usr/bin/python3
"""Unit tests for Square class"""

import json
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests for the Square class"""

    def setUp(self):
        """Set up a few instances of Square for use in tests"""
        self.s1 = Square(5, 1, 2, 10)
        self.s2 = Square(3)

    def test_size(self):
        """Test size attribute"""
        self.assertEqual(self.s1.size, 5)
        self.assertEqual(self.s2.size, 3)

    def test_x(self):
        """Test x attribute"""
        self.assertEqual(self.s1.x, 1)
        self.assertEqual(self.s2.x, 0)

    def test_y(self):
        """Test y attribute"""
        self.assertEqual(self.s1.y, 2)
        self.assertEqual(self.s2.y, 0)

    def test_area(self):
        """Test the area method"""
        self.assertEqual(self.s1.area(), 25)
        self.assertEqual(self.s2.area(), 9)

    def test_update(self):
        """Test the update method with *args"""
        self.s1.update(89, 7, 3, 5)
        self.assertEqual(self.s1.id, 89)
        self.assertEqual(self.s1.size, 7)
        self.assertEqual(self.s1.x, 3)
        self.assertEqual(self.s1.y, 5)

    def test_update_kwargs(self):
        """Test the update method with **kwargs"""
        self.s1.update(size=1, x=3, y=4, id=5)
        self.assertEqual(self.s1.id, 5)
        self.assertEqual(self.s1.size, 1)
        self.assertEqual(self.s1.x, 3)
        self.assertEqual(self.s1.y, 4)

    def test_to_dictionary(self):
        """Test to_dictionary method"""
        s1_dict = self.s1.to_dictionary()
        expected_dict = {'x': 1, 'y': 2, 'id': 10, 'size': 5}
        self.assertEqual(s1_dict, expected_dict)

    def test_save_to_file(self):
        """Test save_to_file method"""
        s1 = Square(5, 1, 2, 10)
        s2 = Square(3, 0, 0, 12)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as file:
            content = file.read()

        expected = json.dumps([s1.to_dictionary(), s2.to_dictionary()])
        # Load both JSON strings as Python objects
        content_loaded = json.loads(content)
        expected_loaded = json.loads(expected)

        # Compare the Python objects
        self.assertEqual(content_loaded, expected_loaded)

    def test_load_from_file(self):
        """Test load_from_file method"""
        s_list = Square.load_from_file()
        self.assertEqual(len(s_list), 2)
        self.assertEqual(s_list[0].size, 5)
        self.assertEqual(s_list[1].size, 3)

    def test_invalid_types(self):
        """Test invalid types for attributes"""
        with self.assertRaises(TypeError):
            Square("5")
        with self.assertRaises(TypeError):
            Square(5, "1")

    def test_invalid_values(self):
        """Test invalid values for attributes"""
        with self.assertRaises(ValueError):
            Square(-5)
        with self.assertRaises(ValueError):
            Square(5, -1)
        with self.assertRaises(ValueError):
            Square(5, 1, -2)


if __name__ == '__main__':
    unittest.main()
