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
        """Getter for size

        Returns:
            int: size
        """
        return self.width

    @size.setter
    def size(self, val):
        """setter for size

        Args:
            val (int): Size
        """
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        """Updates stuff
        """
        if args:
            count = 0
            for val in args:
                if count is 0:
                    self.id = val
                    count += 1
                elif count is 1:
                    self.width = val
                    self.height = val
                    count += 2
                elif count is 3:
                    self.x = val
                    count += 1
                elif count is 4:
                    self.y = val
                    count += 1
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.width = kwargs["size"]
                self.height = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
