#!/usr/bin/python3
"""THis module checks if an object is an instance of a class
or an instance of a class that inherits such given class
"""


def is_kind_of_class(obj, a_class):
    """Checks for object of the a_class or a subclass

    Args:
        obj ([type]): [description]
        a_class ([type]): [description]

    Returns:
        bool: True or False
    """
    return isinstance(obj, a_class)
