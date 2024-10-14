#!/usr/bin/python3
"""
This module defines a class Mylist that inherits from class list,
an inbuilt function in python
"""


class MyList(list):
    """
    A subclass of list that has an additional method to print
    the list in sorted (ascending) order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order without modifying the original list.
        """
        print(sorted(self))
