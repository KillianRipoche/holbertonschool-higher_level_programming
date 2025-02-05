#!/usr/bin/python3
"""Module that contains a function to check
if an object is exactly an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Checks if the object is exactly an instance of the specified class.

    :param obj: The object to check
    :param a_class: The class to compare with
    :return: True if obj is exactly an instance of a_class, otherwise False
    """
    return type(obj) is a_class
