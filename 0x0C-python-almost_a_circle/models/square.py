#!/usr/bin/python3
"""This module contains the square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class square

    Args:
        Rectangle (class): Sub class which is now also a super class
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
              self.width)
