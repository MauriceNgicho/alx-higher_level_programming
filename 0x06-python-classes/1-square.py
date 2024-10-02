#!/usr/bin/python3
"""Defines a class Square with a private instance attribute"""


class Square:
    """Represents a square with a size attribute"""

    def __init__(self, size):
        """Initializes the square with a given size

        Args:
            size: The size of the square.
        """
        self.__size = size
