#!/usr/bin/python3
def remove_char_at(str, n):
    # Return the original string if n is out of range
    if n < 0 or n >= len(str):
        return str
    # Return a new string without the character at index n
    return str[:n] + str[n+1:]
