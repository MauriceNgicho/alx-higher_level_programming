#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        # Loop through the list in reverse order
        for i in reversed(my_list):
            # Print each integer
            print("{:d}".format(i))
