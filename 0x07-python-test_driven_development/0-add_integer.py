#!/usr/bin/python3
"""
This module provides a function add_integer that adds two integers.
The function ensures that the inputs are either integers or floats,
casting floats to integers before performing the addition.
"""

def add_integer(a, b=98):
    """
    Adds two integers.
    
    Args:
        a (int, float): The first number, must be an integer or float.
        b (int, float, optional): The second number, must be an integer or float. Defaults to 98.
        
    Returns:
        int: The addition of a and b after casting them to integers.

    Raises:
        TypeError: If either a or b is neither an integer nor a float.
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
