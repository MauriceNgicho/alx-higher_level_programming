#!/usr/bin/python3
"""
This module defines a JSON function
"""
import json
"""Imports the json inbuilt function"""


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: The object to be serialized into a JSON string.

    Returns:
        A string containing the JSON representation of the object.
    """
    return json.dumps(my_obj)
