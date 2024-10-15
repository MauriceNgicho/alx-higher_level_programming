#!/usr/bin/python3
"""
This module defines a function that inherits from class in an inbuilt functio
"""


class MyInt(int):
    """Class MyInt that inverts the == and != operators."""

    def __eq__(self, other):
        """Override == operator with != behavior."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override != operator with == behavior."""
        return super().__eq__(other)
