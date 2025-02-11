#!/usr/bin/python3
""" read file because this is cool"""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
