#!/usr/bin/python3
def print_square(size):
    """
    Prints a square with the character '#'.

    Args:
        size (int): The size of the square's sides.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.

    Example:
        >>> print_square(4)
        ####
        ####
        ####
        ####
    """
    # Vérification que size est un entier
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Vérification que size est >= 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Imprime un carré de côté 'size' avec le caractère '#'
    for _ in range(size):
        print("#" * size)
