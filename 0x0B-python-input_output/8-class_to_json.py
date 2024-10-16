#!/usr/bin/python3
"""
This module defines a function that returns the dictionary description
with simple data structure(list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    for JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        A dictionary containing the serializable attributes of the object.
    """
    return obj.__dict__
