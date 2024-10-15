#!/usr/bin/python3
"""
This module defines a function that appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """Appends a string to a file and return number of characters added."""
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
