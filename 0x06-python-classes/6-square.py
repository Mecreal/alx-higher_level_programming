#!/usr/bin/python3
"""Square class defines a square and performs size validation. """


class Square:
    """ Square class defines a square and performs size validation. """
    def __init__(self, size=0, position=(0, 0)):
        """ Initializes a Square instance.
        Args: size (int, optional): The size of the square (default is 0).
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0. """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ Get the position"""
        return self.__position

    @position.setter
    def position(self, pos):
        if not self._is_valid_position(pos):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = pos

    def my_print(self):
        val = self.__size
        if val == 0:
            print()
        else:
            print("\n"*self.__position[1], end="")
            for _ in range(val):
                print(" " * self.__position[0] + "#" * val)

    @staticmethod
    def _is_valid_position(value):
        return (
            isinstance(value, tuple) and
            len(value) == 2 and
            all(isinstance(num, int) and num >= 0 for num in value)
        )
