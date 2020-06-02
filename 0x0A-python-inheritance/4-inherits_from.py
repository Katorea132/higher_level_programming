#!/usr/bin/python3
"""THis module contains a function to test if the object
is from a class the inherited directly or indirectly from the given
class
"""


def inherits_from(obj, a_class):
    """Return true if the object is from a subclass from the given
    class

    Args:
        obj (object): The object to test
        a_class (class): The super class which the object can't belong directly

    Returns:
        bool: True or False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
