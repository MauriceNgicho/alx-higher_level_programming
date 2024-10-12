#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_at_end(self):
        """Test when the max integer is at the end of the list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_middle(self):
        """Test when the max integer is at the middle of the list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_one_element(self):
        """Test when the list has only one element"""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Test when the list is empty"""
        self.assertEqual(max_integer([]), None)

    def test_negative_numbers(self):
        """Test a list of negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test a list with both positive and negative numbers"""
        self.assertEqual(max_integer([-1, 3, -4, 2]), 3)

    def test_none_argument(self):
        """Test when None is passed as an argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_no_argument(self):
        """Test when no argument is passed"""
        self.assertEqual(max_integer(), None)


if __name__ == '__main__':
    unittest.main()
