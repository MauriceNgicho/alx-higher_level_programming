#!/usr/bin/python3
"""
This module defines a class Basegeomtry that calculates the area
raise an exceptin if area is not implemented. It also validates integer
and raised an error.

"""


class BaseGeometry:
    """
    A class representing BaseGeometry with
    area and integer validation methods.
    """

    def area(self):
        """
        Raises an Exception with the message that
        area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that `value` is an integer and greater than 0.

        Args:
            name (str): Always a string representing the name of the value.
            value (int): The value to validate.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
