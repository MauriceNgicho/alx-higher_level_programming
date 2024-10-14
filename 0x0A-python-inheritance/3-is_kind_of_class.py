#!/usr/bin/python3
"""
This module defines a function that returns True if the object is an instance
of, or if the object is an instance of a class that inherited from,
the specified class ; otherwise False
"""


def is_kind_of_class(obj, a_class):
    """Check if obj is an instance of a_class or its subclass."""
    return isinstance(obj, a_class)
