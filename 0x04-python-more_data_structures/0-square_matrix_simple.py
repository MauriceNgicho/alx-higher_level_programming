#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create new matrix using list comprehension that squares each element
    return [[x ** 2 for x in row] for row in matrix]
