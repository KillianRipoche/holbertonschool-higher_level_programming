#!/usr/bin/env python3
"""this is a com"""
import json
"""thanks checker"""


def serialize_and_save_to_file(data, filename):
    """
    save file
    """
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Load and deserialize
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
