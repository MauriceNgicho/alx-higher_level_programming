#!/usr/bin/python3
"""Defines a class Square with size validation and area calculation"""


class Square:
    """Represents a square with a size attribute,
    and method to calculate area"""

    def __init__(self, size=0):
        """Initializes the square with an optional size

        Args:
            size (int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates and returns the area of the square

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size
