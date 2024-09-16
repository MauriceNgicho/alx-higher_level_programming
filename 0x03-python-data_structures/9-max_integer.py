#!/usr/bin/python3
def max_integer(my_list=[]):
    # Check if the list is empty
    if len(my_list) == 0:
        return None   # Return None if the list is empty

    # Assume the first element is the maximum value
    max_value = my_list[0]
    for num in my_list:
        if num > max_value:
            max_value = num
    return max_value
