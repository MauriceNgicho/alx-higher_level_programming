#!/usr/bin/python3
"""Unit tests for Base class"""

import json
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests for Base class"""

    def test_to_json_string(self):
        """Test to_json_string with valid input"""
        list_dict = [{'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8}]
        json_dict = Base.to_json_string(list_dict)

        expected = json.dumps(list_dict)

        json_dict_loaded = json.loads(json_dict)
        expected_loaded = json.loads(expected)

        self.assertEqual(json_dict_loaded, expected_loaded)

    def test_to_json_string_empty(self):
        """Test to_json_string with None or empty list"""
        self.assertEqual(Base.to_json_string(None), '[]')
        self.assertEqual(Base.to_json_string([]), '[]')

    def test_from_json_string(self):
        """Test from_json_string with valid input"""
        json_string = '[{"x": 2, "y": 8, "id": 1, "width": 10, "height": 7}]'
        list_output = Base.from_json_string(json_string)
        self.assertEqual(list_output, [{"x": 2, "y": 8, "id": 1,
                                        "width": 10, "height": 7}])

    def test_from_json_string_empty(self):
        """Test from_json_string with None or empty string"""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(''), [])

    def test_create(self):
        """Test create method to create instance from dictionary"""
        rect_dict = {'id': 89, 'width': 10, 'height': 4, 'x': 1, 'y': 2}
        rect = Rectangle.create(**rect_dict)
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 4)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 2)

    def test_load_from_file(self):
        """Test load_from_file method with Rectangle"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rects = [r1, r2]
        Rectangle.save_to_file(list_rects)

        loaded_rects = Rectangle.load_from_file()
        self.assertEqual(len(loaded_rects), 2)
        self.assertEqual(loaded_rects[0].width, 10)
        self.assertEqual(loaded_rects[1].width, 2)


if __name__ == '__main__':
    unittest.main()
