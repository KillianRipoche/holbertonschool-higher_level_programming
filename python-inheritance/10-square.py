#!/usr/bin/python3
"""class square """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class of a square"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return super().area()

    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
