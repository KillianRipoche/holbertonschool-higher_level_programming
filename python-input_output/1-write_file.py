#!/usr/bin/python3
"""write in file because this is cool"""


def write_file(filename="", text=""):
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
