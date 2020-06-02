#!/usr/bin/python3
"""This module contains a function to check if an object is of the same
class than a given class
"""


def is_same_class(obj, a_class):
    """Checks if an object is of the same class

    Args:
        obj (object): Object to check
        a_class (class): Class to compare to

    Returns:
        bool: True or False
    """
    return type(obj) == a_class
