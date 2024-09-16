#!/usr/bin/python3
def delete_at(my_list=[], idx=0):

    # Check if idx is valid
    if idx < 0 or idx >= len(my_list):
        return my_list   # Return original list if idx is not valid

    # Delete item at specified index
    del my_list[idx]

    # Return modified list
    return my_list
