#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        # Print each row
        for i in range(len(row)):
            if i == len(row) - 1:
                # Print last element without space
                print("{:d}".format(row[i]), end="")
            else:
                # Print each element followed by a space
                print("{:d}".format(row[i]), end=" ")
        print()   # Print new line after each row
