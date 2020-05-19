#!/usr/bin/python3
"""A file to declare a square and it's size"""

class Square:
    """
    A square class with it's size

    Attributes:
        _size (int): Holds the size of the square, private.
    """
    def __init__(self, size):
        """This initializes the private value size"""
        self.__size = size
