#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []

    # Iterate over each element in the list
    for i in my_list:

        # Check if the element is divisible by 2
        if i % 2 == 0:
            result.append(True)
        else:
            result.append(False)

    # Return the new lis
    return result
