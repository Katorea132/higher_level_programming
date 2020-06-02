#!/usr/bin/python3
"""This module holds a function that calls the dir function
"""


def lookup(obj):
    """Returns a lists of all the attributes and methods

    Args:
        obj (object): Holds the object

    Returns:
        list: A list of attributes and methods
    """
    return dir(obj)
