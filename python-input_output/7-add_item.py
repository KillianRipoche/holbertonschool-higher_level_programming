#!/usr/bin/python3
"""com before the import for the checker"""
import json
import sys


def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as file:
        return json.dump(my_obj, file)


def load_from_json_file(filename):
    with open(filename, encoding='utf-8') as file:
        return json.load(file)


def add_args_to_json():
    try:
        my_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        my_list = []

    my_list.extend(sys.argv[1:])

    save_to_json_file(my_list, "add_item.json")


if __name__ == "__main__":
    add_args_to_json()
