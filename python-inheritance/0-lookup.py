#!/usr/bin/python3
"""
    This module provides a function to list all available attributes and methods of an object.
    Returns:
    list: A list of attribute and method names available in the object.
    """


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.
    Args:
        obj: The object to inspect.
    """

    return dir(obj)
