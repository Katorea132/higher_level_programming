#!/usr/bin/python3
"""This module has a function that returns the dict method
of an object
"""


def class_to_json(obj):
    """dict to a json

    Args:
        obj (object): The object to see the dict from

    Returns:
        dict: Dictionary of all methods and attributes
    """
    return obj.__dict__
