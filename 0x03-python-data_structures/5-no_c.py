#!/usr/bin/python3
def no_c(my_string):
    result = ""   # Create an empty string

    # Iterate through each character of the original string
    for chr in my_string:
        if chr != 'c' and chr != 'C':
            result += chr

    # Return the modified string
    return result
