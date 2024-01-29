#!/usr/bin/python3
"""
This module provides a function say_my_name for printing names.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first name> <last name>

    Args:
        first_name: string, the first name.
        last_name: string, The last name.

    Raises:
        TypeError: If the first_name or last_name is not a string.
    """

    if not isinstance(first_name, (str)):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, (str)):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
