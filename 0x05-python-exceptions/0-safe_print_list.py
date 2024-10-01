#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0  # To track the number of elements printed
    try:
        for i in range(x):  # Iterate up to x elements
            print(my_list[i], end="")  # Print element without a newline
            count += 1  # Increment count if successful
    except IndexError:
        pass  # Ignore index errors when x exceeds the list length
    print()  # Print a newline after all elements are printed
    return count
