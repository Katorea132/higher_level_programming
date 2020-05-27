#!/usr/bin/python3
""" This module contains a function to print squares :D
"""


def print_square(size):
    """Prints squares

    Args:
        size (int): Holds the size

    Raises:
        TypeError: In case size is not an integer
        ValueError: In case size is less than 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print((("#" * size + "\n") * size), end="")
