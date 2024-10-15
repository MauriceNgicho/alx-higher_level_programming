#!/usr/bin/python3
"""
This module represent a function that returns
an object represented by json string
"""
import json
"""Import json"""


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str: The JSON string to be converted into a Python object.

    Returns:
        The corresponding Python object (list, dict, etc.).
    """
    return json.loads(my_str)
