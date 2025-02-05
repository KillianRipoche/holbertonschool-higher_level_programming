#!/usr/bin/python3
"""
This module defines a class MyList
"""


class MyList(list):
    """
    A subclass of list that includes a method to print the list sorted.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """
        print(sorted(self))
