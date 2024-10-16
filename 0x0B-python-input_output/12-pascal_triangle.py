#!/usr/bin/python3
"""
This module defines a function of pascals triangle
"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal’s triangle of n.

    Args:
        n (int): The number of rows in Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # First row is always [1]

    for i in range(1, n):
        prev_row = triangle[-1]
        # Create the next row based on the previous row
        row = [1]  # Start with 1
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])  # Sum of the two elements above
        row.append(1)  # End with 1
        triangle.append(row)

    return triangle

