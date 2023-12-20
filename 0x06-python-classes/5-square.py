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
        self.__size = size

    def area(self):
        return self.__size**2

    @property
    def size(self):
        """ Get the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        val = self.__size
        if val == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
