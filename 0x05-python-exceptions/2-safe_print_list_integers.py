#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            # Print if the element is an integer
            print("{:d}".format(my_list[i]), end="")
            count += 1  # Increment count for each successfully printed integer
        except (ValueError, TypeError):
            # Skip the element if it's not an integer
            continue
        except IndexError:
            # Break the loop if the index is out of range
            break
    print()
    return count  # Return the number of integers printed
