#!/usr/bin/python3
"""
This module defines a class Basegeomtry that calculates the area
raise an exceptin if area is not implemented.
"""


class BaseGeometry:
    """A class representing Basegeometry."""
    def area(self):
        """Raises an exception with message ara() is not implemented."""
        raise Exception("area() is not implemented")
