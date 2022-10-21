#!/usr/bin/python3
"""
This is the 2-matrix_divided module.
The function matrix_divided(matrix, div) divides all elements of a matrix.
"""

def matrix_divided(matrix, div):
    """Divides all elements of a matrix.
    Args:
    - matrix (list of list)
    - div (int or float)
    The lists inside of the matrix must be of the same size.
    Return a new matrix with the elements divided by a int or float.
    """
    new_matrix = []
    long_error = 'matrix must be a matrix (list of lists) of integers/floats'

    if not isinstance(matrix, list):
        raise TypeError(long_error)

    if (type(div) not in [int, float]):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    if len(matrix) == 0:
        return new_matrix

    elements = len(matrix[0])

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(long_error)

        if len(row) != elements:
            raise TypeError('Each row of the matrix must have the same size')

        for num in row:
            if (type(num) not in [int, float]):
                raise TypeError(long_error)

        new_matrix.append(list(map(lambda num: round(num / div, 2), row)))

    return new_matrix
