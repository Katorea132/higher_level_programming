#!/usr/bin/python3
"""
This will initialize a square, checking for an adecuate size value
and type
"""


class Square:
    """
    Class to define a square with propper size
    """
    def __init__(self, size=0):
        """Initializes the size

        Args:
            size (int): Holds the size, must be a number not
            below 0. Defaults to 0.
        Raises:
            TypeError: In case value is not an int
            ValueError: In case value is below 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns the area according to the size

        Returns:
            int: area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """Getter for size

        Returns:
            int: Size of the square
        """
        return self.__size

    @size.setter
    def size(self, siz):
        """setter for size

        Args:
            siz (int): New size of square, must be 0 or above, also
            a number

        Raises:
            TypeError: When value is not an integer
            ValueError: When value is below 0
        """
        if type(siz) is not int:
            raise TypeError("size must be an integer")
        elif siz < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = siz
