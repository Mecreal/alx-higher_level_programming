#!/usr/bin/python3
"""
This module provides a function that prints a square with the character #.
"""


def print_square(size):
    """
    print the square with #
    
    Args:
        size: int, size of the square.


    Raises:
        TypeError: if size is less than 0.
        TypeError: size is a float and is less than 0
        TypeError: size is a float and is less than 0
    """
    if not isinstance(size, (int)):
        raise TypeError("size must be an integer")
    
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
