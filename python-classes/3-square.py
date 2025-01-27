#!/usr/bin/python3
""" Create a new class, we'll define it with size
"""


class Square:
    """this is a square with size and error
    """

    def __init__(self, size=0):

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size
