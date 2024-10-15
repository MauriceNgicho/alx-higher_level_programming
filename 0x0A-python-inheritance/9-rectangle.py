#!/usr/bin/python3
"""
This module defines a class Rectangle that inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Iports BaseGeometry"""


class Rectangle(BaseGeometry):
    """Class that represents a rectangle, inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """Initializes the Rectangle with width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        
        self.__width = width
        self.__height = height

    def area(self):
        """Implements the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns the rectangle description."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
