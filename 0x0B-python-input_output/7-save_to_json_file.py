#!/usr/bin/python3
"""SAves an object to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """Saves an object

    Args:
        my_obj ([type]): [description]
        filename ([type]): [description]
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
