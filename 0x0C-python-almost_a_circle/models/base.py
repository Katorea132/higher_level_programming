#!/usr/bin/python3
"""This module constains a class called Base
"""


class Base:
    """This is the Base class, behold!
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
