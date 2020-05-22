#!/usr/bin/python3
"""This module contains a function in charge
of dividing a matrix (list of list) that must contain
either integers or floats
"""


def matrix_divided(matrix, div):
    """THis divides a list of list that contain either integers or floats

    Args:
        matrix (list of lists): Contains the matrix
        div (integer, float): The number to divide, must not ve 0

    Raises:
        TypeError: In case the contents sent are not a list of lists with ints
        or flaots
        TypeError: In case the dividing number isn't a number (float or int)
        ZeroDivisionError: When dividing by 0

    Returns:
        List of lists: the results of the divisions
    """
    error = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or not matrix:
        raise TypeError(error)
    for x in matrix:
        if type(x) is not list or not x:
            raise TypeError(error)
        elif len(x) is not len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for y in x:
            if type(y) not in [int, float]:
                raise TypeError(error)
    if div is None or type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    return [[round(y/div, 2) for y in x] for x in matrix]
