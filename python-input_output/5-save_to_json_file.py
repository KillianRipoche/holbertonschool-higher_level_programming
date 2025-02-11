#!/usr/bin/python3
"""com before the import for the checker"""
import json


def save_to_json_file(my_obj, filename):
    """json.dump checker"""
    with open(filename, 'w') as file:
        return json.dump(my_obj, file)
