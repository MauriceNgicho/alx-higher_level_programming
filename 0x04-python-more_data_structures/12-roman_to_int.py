#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    # Mapping of Roman numerals to integers
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    length = len(roman_string)

    for i in range(length):
        # If the current character is smaller than the next one, it's a subtraction case
        if i < length - 1 and roman_dict[roman_string[i]] < roman_dict[roman_string[i + 1]]:
            total -= roman_dict[roman_string[i]]
        else:
            total += roman_dict[roman_string[i]]

    return total
