#!/usr/bin/python3
"""Square class defines a square and performs size validation. """


class Square:
    """ Square class defines a square and performs size validation. """
    def __init__(self, size=0):
        """ Initializes a Square instance.
        Args: size (int, optional): The size of the square (default is 0).
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0. """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size**2       
