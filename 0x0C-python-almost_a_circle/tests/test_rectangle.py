#!/usr/bin/python3
"""Unit tests for Rectangle class"""

import json
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for the Rectangle class"""

    def setUp(self):
        """Set up a few instances of Rectangle for use in tests"""
        self.r1 = Rectangle(10, 2, 1, 9, 1)
        self.r2 = Rectangle(2, 4)

    def test_width(self):
        """Test width attribute"""
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r2.width, 2)

    def test_height(self):
        """Test height attribute"""
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r2.height, 4)

    def test_x(self):
        """Test x attribute"""
        self.assertEqual(self.r1.x, 1)
        self.assertEqual(self.r2.x, 0)

    def test_y(self):
        """Test y attribute"""
        self.assertEqual(self.r1.y, 9)
        self.assertEqual(self.r2.y, 0)

    def test_area(self):
        """Test the area method"""
        self.assertEqual(self.r1.area(), 20)
        self.assertEqual(self.r2.area(), 8)

    def test_update(self):
        """Test the update method with *args"""
        self.r1.update(89, 5, 3, 2, 6)
        self.assertEqual(self.r1.id, 89)
        self.assertEqual(self.r1.width, 5)
        self.assertEqual(self.r1.height, 3)
        self.assertEqual(self.r1.x, 2)
        self.assertEqual(self.r1.y, 6)

    def test_update_kwargs(self):
        """Test the update method with **kwargs"""
        self.r1.update(width=1, height=2, x=3, y=4, id=5)
        self.assertEqual(self.r1.id, 5)
        self.assertEqual(self.r1.width, 1)
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r1.x, 3)
        self.assertEqual(self.r1.y, 4)

    def test_to_dictionary(self):
        """Test to_dictionary method"""
        r1_dict = self.r1.to_dictionary()
        expected_dict = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(r1_dict, expected_dict)

    def test_save_to_file(self):
        """Test save_to_file method"""
        r1 = Rectangle(10, 2, 1, 9, 1)
        r2 = Rectangle(2, 4, 0, 0, 14)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            content = file.read()

        expected = json.dumps([r1.to_dictionary(), r2.to_dictionary()])

        content_loaded = json.loads(content)
        expected_loaded = json.loads(expected)

        self.assertEqual(content_loaded, expected_loaded)

    def test_load_from_file(self):
        """Test load_from_file method"""
        r_list = Rectangle.load_from_file()
        self.assertEqual(len(r_list), 2)
        self.assertEqual(r_list[0].width, 10)
        self.assertEqual(r_list[1].width, 2)

    def test_invalid_types(self):
        """Test invalid types for attributes"""
        with self.assertRaises(TypeError):
            Rectangle("10", 2)
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

    def test_invalid_values(self):
        """Test invalid values for attributes"""
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)
        with self.assertRaises(ValueError):
            Rectangle(10, -2)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -1)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 1, -9)


if __name__ == '__main__':
    unittest.main()
