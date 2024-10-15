#!/usr/bin/python3
"""
This module defines a function that reads a text and prints it to stdout
"""


def read_file(filename=""):
    """Reads a UTF-8 encoded text file and prints it to stdout."""
    with open(filename, mode='r', encoding='utf-8') as f:
        print(f.read(), end="")
