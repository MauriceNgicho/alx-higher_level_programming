#!/usr/bin/python3
"""
This module defines a function that writes an object to a text file
using JSON representation
"""
import json
"""Import json"""


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file, using its JSON representation.

    Args:
        my_obj: The Python object to be serialized and written to the file.
        filename: The name of the file to which the object will be written.
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)
