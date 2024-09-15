#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):

    # Reverse the list
    my_list = list(reversed(my_list))

    # Print each integer
    for i in my_list:
        print("{}".format(i))
