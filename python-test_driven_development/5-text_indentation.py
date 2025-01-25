#!/usr/bin/python3
"""
    Prints a text with 2 new lines after each '.', '?', and ':'.

    Args:
        text: The input text (must be a string).

    Raises:
        TypeError: If text is not a string.
"""


def text_indentation(text):
    """
    indenting a text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    flag = 1
    for letter in text:
        if flag == 1:
            if letter == ' ':
                continue
            else:
                flag = 0
        print(letter, end="")
        if letter in ".?:":
            print("\n")
            flag = 1
