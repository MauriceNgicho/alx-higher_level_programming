#!/usr/bin/python3
"""
This module provides a function that prints text with 2 new lines after
each of the characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after
            each of the characters: '.', '?' and ':'.

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize an empty string to accumulate the formatted text
    formatted_text = ""

    # Iterate over each character in the text
    i = 0
    while i < len(text):
        formatted_text += text[i]

        if text[i] in ['.', '?', ':']:
            formatted_text += '\n\n'
            # Skip any spaces following the character
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue

        i += 1

    # Strip any extra spaces at the beginning or end of each line and print
    lines = formatted_text.splitlines()
    for line in lines:
        print(line.strip())
