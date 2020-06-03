#!/usr/bin/python3
"""THis module contains a function to make a json file out
of a string
"""
import json


def to_json_string(my_obj):
    """Returns a json out of a string

    Args:
        my_obj (object): The soon to be json 

    Returns:
        json: RepresensaTION
    """
    return json.dumps(my_obj)
