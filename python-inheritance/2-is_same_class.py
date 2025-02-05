#!/usr/bin/python3
"""
This module provides a function to check if an object is exactly an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class.
    """
    return type(obj) is a_class
