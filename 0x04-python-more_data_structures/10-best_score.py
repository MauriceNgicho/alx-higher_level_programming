#!/usr/bin/python3
def best_score(a_dictionary):
    # Return None if the dictionary is empty
    if not a_dictionary:
        return None
    # Use max() to find the key with the largest value
    return max(a_dictionary, key=a_dictionary.get)
