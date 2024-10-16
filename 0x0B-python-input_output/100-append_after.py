#!/usr/bin/python3
"""
This module defines a function that inserts a line of text to a file
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts new_string after each line containing
    search_string in the file"""
    with open(filename, 'r') as f:
        lines = f.readlines()

    with open(filename, 'w') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
