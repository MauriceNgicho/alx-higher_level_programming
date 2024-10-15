#!/usr/bin/python3
"""
This module defines a class square that inherits from Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle
"""Imports Rectangle"""


class Square(Rectangle):
    """Class that represents a square, inheriting from Rectangle."""

    def __init__(self, size):
        """Initializes the square with size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Implements the area of the square."""
        return self.__size * self.__size
