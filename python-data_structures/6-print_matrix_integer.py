#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for num in matrix:
        for i, element in enumerate(num):
            print("{:d}".format(element), end=" " if i < len(num) - 1 else "")

        print()
