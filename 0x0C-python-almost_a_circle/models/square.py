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
        """Initializer/Constructor

        Args:
            size (int): Size of a side
            x (int, optional): X. Defaults to 0.
            y (int, optional): Y. Defaults to 0.
            id (int): ID. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Prints pretty

        Returns:
            str: Pretty format
        """
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, val):
        self.width = val
        self.height = val
