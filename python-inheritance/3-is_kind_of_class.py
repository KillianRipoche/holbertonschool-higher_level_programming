#!/usr/bin/python3
"""
This module provides a function to check if an object is an instance of a class
or an instance of a class that inherited from the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of a class or a subclass.
    """
    return isinstance(obj, a_class)
