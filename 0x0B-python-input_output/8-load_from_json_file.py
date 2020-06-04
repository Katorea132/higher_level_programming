#!/usr/bin/python3
"""THis module contains a function to bring a JSON
from a document
"""
import json


def load_from_json_file(filename):
    """Returns the dict from a json in a file

    Args:
        filename (string): Filename

    Returns:
        dict: the data from the json
    """
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data
