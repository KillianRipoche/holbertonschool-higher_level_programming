#!/usr/bin/python3
"""
    Returns the list of available attributes and methods of an object.
    :param obj: The object to inspect
    :return: List of attributes and methods
    """


def lookup(obj):
    """ returns the list of available attributes and methods of an object"""
    return dir(obj)
