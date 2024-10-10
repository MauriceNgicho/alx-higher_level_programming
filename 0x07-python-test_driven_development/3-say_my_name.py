#!/usr/bin/python3
"""
This module provides a function that prints a name
"""


def say_my_name(first_name, last_name=""):
    """
    prints 'My name is <first_name> <last_name>'


    Args:
        first_name (str): The first name to print.
        last_name (str): The last name to print (optional).


    Raises:
        TypeError: If first_name or Last_name are not string.
    """


    # check if first_name is a string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")


    # check if last name is a string
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")


    # print full name
    print("My name is {} {}".format(first_name, last_name))
