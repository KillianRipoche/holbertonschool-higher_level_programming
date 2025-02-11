#!/usr/bin/python3
"""com before the import for the checker"""
import json


def load_from_json_file(filename):
    """json.load checker"""
    with open(filename, encoding="utf-8") as file:
        return json.load(file)
