#!/usr/bin/python3
def replace_in_list(my_list, idx, element):

    # Check if the index is valid
    if idx < 0 or idx >= len(my_list):

        # Return original list if index is invalid
        return my_list

    # Replace element at a specified index in the list
    my_list[idx] = element

    # Return the new list
    return my_list
