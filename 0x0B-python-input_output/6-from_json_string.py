#!/usr/bin/python3
"""Module to get a string from a json
"""
import json


def from_json_string(my_str):
    """A string from a JSON

    Args:
        my_str (JSON): the thing to be a string

    Returns:
        dict: the string
    """
    return json.loads(my_str)
