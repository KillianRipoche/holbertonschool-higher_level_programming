#!/usr/bin/python3
"""com checker"""


class Student:
    """
    A student class for the checker
    """

    def __init__(self, first_name, last_name, age):
        """init for student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """get attribute and check value"""
        if isinstance(attrs, list) and all(isinstance(attr, str)
                                           for attr in attrs):
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
        return self.__dict__

    def reload_from_json(self, json):
        """load value with key"""
        for key, value in json.items():
            setattr(self, key, value)
