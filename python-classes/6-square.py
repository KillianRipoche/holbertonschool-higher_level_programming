#!/usr/bin/python3
""" Create a new class, we'll define it with size
"""


class Square:
    """this is a square with size and error
    """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """getter for size value"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ getter for position value"""
        return self.__position

    @position.setter
    def position(self, value):
        """ Setter to modify the position """
        if (not isinstance(value, tuple) or len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        """Affiche le carré avec le caractère '#' en prenant en compte la position"""
        if self.__size == 0:
            print()
            return

        [print() for _ in range(self.__position[1])]

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
