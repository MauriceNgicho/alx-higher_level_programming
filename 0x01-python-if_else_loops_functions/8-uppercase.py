#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            # Convert to uppercase by subtracting 32 from the ASCII value
            uppercase_char = chr(ord(c) - 32)
        else:
            uppercase_char = c
        print("{}".format(uppercase_char), end="")
    print()
