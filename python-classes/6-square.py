#!/usr/bin/python3
""" Create a new class, we'll define it with size
"""


class Square:
    """define a square with a size and a position"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square at 0 and the position too"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """get size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """change the size of teh square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """get the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """change the position of the square with value"""
        if (not isinstance(value, tuple) or len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """return the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the good position"""
        if self.__size == 0:
            print()
            return

        [print() for _ in range(self.__position[1])]

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
