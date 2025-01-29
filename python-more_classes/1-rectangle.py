#!/usr/bin/python3
""" Create a new class, we'll define it later
"""


class Rectangle:
    """ an empty rectangle, we will define it later too
    """

    def __init__(self, width=0, height=0):
        """initialize the rectangle with width and height at 0"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """get width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """change the size of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """ change the height of the rectangle with the value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
