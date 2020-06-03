#!/usr/bin/python3
"""BOI IF I CAN
"""


def add_attribute(obj, name, value):
    """Sets attribute if possible

    Args:
        obj (object): Holds the object to add the attribute to
        name (str): The name of the attribute
        value (None): The value to add, could be anything

    Raises:
        TypeError: If can't add attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
