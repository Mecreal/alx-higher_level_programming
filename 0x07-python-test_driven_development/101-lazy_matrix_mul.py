#!/usr/bin/python3
"""
lazy matrix math
"""

import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy's matmul function.

    Args:
        m_a (list of list of floats or ints): The first matrix.
        m_b (list of list of floats or ints): The second matrix.

    Returns:
        numpy.ndarray: The result of the matrix multiplication.
    """
    return numpy.matmul(m_a, m_b)
