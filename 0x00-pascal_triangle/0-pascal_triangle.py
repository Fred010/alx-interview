#!usr/bin/python3


def pascal_triangle(n):
    """
    This function generates Pascal's Triangle up to n rows

    Args:
    n: The number of rows in a triangle - integer

    Returns:
    A list of lists containing the Pascal's Triangle
    Returns an empty list if n <= 0
    """

    triangle = []
    if n <= 0:
        return triangle

    triangle.append([1])

    for x1 in range(1, n):
        row = [1]
        prev_row = triangle[x1 - 1]

        for x2 in range(1, x1):
            row.append(prev_row[x2 - 1] + prev_row[x2])

        row.append(1)
        triangle.append(row)

    return triangle
