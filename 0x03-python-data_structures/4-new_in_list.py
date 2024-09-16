#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    # A copy of the original
    new_list = my_list[:]

    # Check if the index range is valid
    if idx < 0 or idx >= len(my_list):
        return new_list   # Return copy of original if index is out of range
    # Replace the element at the given index
    new_list[idx] = element
    return new_list
