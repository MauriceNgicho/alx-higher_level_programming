#!/usr/bin/python3
"""
This object creates a function thta adds attribute
"""


def add_attribute(obj, name, value):
    """Adds a new attribute to an object if possible."""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
