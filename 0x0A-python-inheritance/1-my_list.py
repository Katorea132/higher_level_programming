#!/usr/bin/python3
"""THis module contains a class that inherits from lists
that has a function to print sorted lists
"""


class MyList(list):
    """This class inherits fron lists
    """
    def print_sorted(self):
        """This prints itself sorted
        """
        print(sorted(self))
