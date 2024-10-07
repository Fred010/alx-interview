#!/usr/bin/python3
"""
A module for working with Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to n rows.

    Args:
    n: The number of rows in the triangle - int

    Returns:
    A list of lists containing the Pascal's Triangle.
    Returns an empty list if n <= 0.
    """

    triangle = []
    if type(n) is not int or n <= 0:
                return triangle
    for row in range(n):
        if row == 0:
            triangle.append([1])
        else:
            triangle.append(
                    [1] +
                    [triangle[row-1][i] + triangle[row-1][i+1] for i in range(
                        row-1)] + [1])
    return triangle
