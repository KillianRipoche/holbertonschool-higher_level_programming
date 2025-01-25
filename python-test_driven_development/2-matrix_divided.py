#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists of int/float): The matrix to divide.
        div (int or float): The number to divide by.

    Returns:
        list of lists of float: A new matrix with the divided elements, rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If each row of the matrix is not of the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """
    # Vérification que `matrix` est une liste de listes de nombres
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not all(all(isinstance(element, (int, float)) for element in row) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    # Vérification que toutes les lignes ont la même taille
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Vérification que `div` est un nombre
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Vérification que `div` n'est pas égal à 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Création d'une nouvelle matrice avec les éléments divisés par `div`
    return [[round(element / div, 2) for element in row] for row in matrix]
