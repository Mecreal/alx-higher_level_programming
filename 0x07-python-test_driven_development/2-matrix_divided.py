#!/usr/bin/python3
"""
This module provides a function matrix_divided for dividing all elements
of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
        matrix: list of lists of int/float, the matrix to divide.
        div: int/float, the divisor.

    Returns:
        A new matrix with each element divided by div, rounded to 2 decimal
        places.

    Raises:
        TypeError: If the divisor is not a number, or if the matrix is not a
                   matrix (list of lists) of integers/floats, or if rows of the
                   matrix are not of the same size.
        ZeroDivisionError: If the divisor is zero.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if (not isinstance(matrix, list) or
        not all(isinstance(row, list) and
                all(isinstance(el, (int, float)) for el in row)
                for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    return [[round(el / div, 2) for el in row] for row in matrix]
