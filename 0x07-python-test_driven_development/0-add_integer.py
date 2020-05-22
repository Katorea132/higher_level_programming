#!/usr/bin/python3
"""
This module contains a function to add 2 numbers casted to integers
they must be floats or integers in the first place
"""


def add_integer(a, b=98):
    """This function adds 2 integers or floats (casted to ints)

    Args:
        a (float, int): The first value
        b (float, int): The second value. Defaults to 98.

    Raises:
        TypeError: if a is not a float or an int
        TypeError: if b is not a float or an int

    Returns:
        int: result of the  addition
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
