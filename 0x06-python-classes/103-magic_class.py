#!/usr/bin/python3
"""This is a magic class
"""
import math


class MagicClass():
    """This is the magic class
    """
    def __init__(self, radius=0):
        """Initializer for radious

        Args:
            radius (int): THis hols the radius. Defaults to 0.

        Raises:
            TypeError: In case of faulty value
        """
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self._MagicClass__radius = radius

    def area(self):
        """Returns the area

        Returns:
            int: Returns the area
        """
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """Returns the circumference

        Returns:
            int: the circumference
        """
        return 2 * math.pi * self._MagicClass__radius
