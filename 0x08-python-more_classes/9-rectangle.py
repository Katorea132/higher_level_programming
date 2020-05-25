#!/usr/bin/python3
"""THis defines a rectangle
"""


class Rectangle:
    """This is a basic rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializer/COnstructor

        Args:
            width (int): Uses the setter for the property width
            height (int): Samebut with height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """property of width

        Returns:
            int: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter of width

        Args:
            value (int): Sets width to this value

        Raises:
            TypeError: If value is not an int
            ValueError: If value is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """property of height

        Returns:
            int: private height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height

        Args:
            value (int): value to be the height

        Raises:
            TypeError: In case value is not an int
            ValueError: In case value is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area

        Returns:
            int: the area
        """
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter

        Returns:
            int: the perimeter
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """An unnofiical string, pretty for the user

        Returns:
            str: the representation of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return ""
        ret = (("{}".format(self.print_symbol) *
               self.width + "\n") * self.height)
        return ret[:-1]

    def __repr__(self):
        """An official string representing the thingy

        Returns:
            str: the official thingy to recreate the object
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Sayounara, rectangle-san
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """Checks whether rect 1 or 2 is bigger

        Args:
            rect_1 (Rectangle): rectangle 1
            rect_2 (Rectangle): rectangle 2

        Raises:
            TypeError: In case either rectangle isn't an actual Rectangle

        Returns:
            Rectangle: the rect1 if equal or bigger or rect 2 if bigger
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Makes a square

        Args:
            size (int): The size of the square. Defaults to 0.

        Returns:
            Rectangle: with the given size as a square
        """
        return cls(size, size)
