#!/usr/bin/python3
"""
This module defines a function that creates an object from a JSON file
"""
import json
"""Import json"""


def load_from_json_file(filename):
    """
    Creates an object from a "JSON file".

    Args:
        filename: The name of the file containing JSON data.

    Returns:
        The Python object represented by the JSON data in the file.
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        return json.load(f)
