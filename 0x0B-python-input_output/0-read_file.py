#!/usr/bin/python3
"""This module constains a function to read and print the
contents of a file with utf 8 encoding
"""


def read_file(filename=""):
    """Prints the file

    Args:
        filename (str): The name of the object file. Defaults to "".
    """
    with open(filename) as f:
        print(f.read(), end="")
