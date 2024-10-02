#!/usr/bin/python3
"""Defines a class Square with a getter and setter for size,
and area calculation."""


class Square:
    """Represents a square with a size attribute,
    and methods to calculate area"""

    def __init__(self, size=0):
        """Initializes the square with an optional size

        Args:
            size (int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size  # Invokes the setter method for validation

    @property
    def size(self):
        """Retrieves the size of the square

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the area of the square

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size
