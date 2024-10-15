#!/usr/bin/python3
"""
This module defines a class Rectangle that inherits from class BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Imports BaseGeometry"""


class Rectangle(BaseGeometry):
    """Class that represents a rectangle and inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initializes the Rectangle with width and height, validates them."""
        # Validate width and height using integer_validator from BaseGeometry
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        # Private attributes
        self.__width = width
        self.__height = height
