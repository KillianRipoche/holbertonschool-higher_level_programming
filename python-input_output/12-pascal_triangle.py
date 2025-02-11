#!/usr/bin/python3
"""this is a triangle"""


def pascal_triangle(n):
    """check if n <= 0"""
    if n <= 0:
        return []

    triangle = []
    for i in range(n):

        add = [None] * (i + 1)
        add[0] =   add[-1] = 1

        for j in range(1, i):
            add[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(add)

    return triangle
