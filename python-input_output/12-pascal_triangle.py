#!/usr/bin/python3
"""this is a triangle"""


def pascal_triangle(n):
    """check if n <= 0"""
    if n <= 0:
        return []

    triangle = []
    for i in range(n):

        row = [None] * (i + 1)
        row[0] = row[-1] = 1

        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle
