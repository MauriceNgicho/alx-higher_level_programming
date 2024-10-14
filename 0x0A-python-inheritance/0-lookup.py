#!/usr/bin/python3
"""
This module defines a function that print list of variable attributes
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.
    """
    return dir(obj)
