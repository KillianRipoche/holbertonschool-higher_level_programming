#!/usr/bin/python3
"""Module defining geometric classes: BaseGeometry, Rectangle, and Square."""


class BaseGeometry:
    """Base Geometry class with validation methods."""

    def area(self):
        """Raises an Exception because it must be implemented in subclasses."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that 'value' is an integer greater than 0.

        :param name: The name of the variable (as a string).
        :param value: The value to be validated.
        :raises TypeError: If 'value' is not an integer.
        :raises ValueError: If 'value' is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle class inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """
        Initializes a rectangle with validated width and height.

        :param width: The width of the rectangle (must be a positive integer).
        :param height: The height of the rectangle (must be positive integer).
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Computes and returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns a formatted string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """Square class inheriting from Rectangle."""

    def __init__(self, size):
        """
        Initializes a square with a validated size.

        :param size: The side length of the square (must be positive integer).
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Computes and returns the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Returns a formatted string representation of the square."""
        return f"[Square] {self.__size}/{self.__size}"
