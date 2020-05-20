#!/usr/bin/python3
"""
This will initialize a square, checking for an adecuate size value
and type
"""


class Square:
    """
    Class to define a square with propper size
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square

        Args:
            size (int): Size of square. Defaults to 0.
            position (tuple): position of square. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

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

    def my_print(self):
        """Prints a square or an empty line if size 0
        """
        r = range(self.__size)
        p = range(self.__position[0])
        if self.__size == 0:
            print()
        else:
            if self.position == (0, 0):
                print("\n".join(["".join(["#" for i in r]) for y in r]))
            else:
                for _ in range(self.__position[1]):
                    print()
                for _ in r:
                    print("".join([" " for s in p]), end="")
                    print("".join(["#" for i in r]))

    @property
    def position(self):
        """Getter of position

        Returns:
            tuple: The position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """position setter

        Args:
            value (tuple): determines the position

        Raises:
            TypeError: checks for the tuple to have adecuate values
        """
        if type(value) is not tuple or len(value) is not 2 or\
            type(value[0]) is not int or value[0] < 0 or\
                type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def __str__(self):
        r = range(self.__size)
        ret = ""
        if self.size == 0:
            return ""
        else:
            ret += "\n" * self.__position[1]
            for _ in r:
                ret += (" " * self.__position[0]) + ("#" * self.__size) + "\n"
        return ret[:-1]
