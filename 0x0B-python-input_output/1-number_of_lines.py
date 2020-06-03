#!/usr/bin/python3
"""This module contains a function to count lines in a file
"""


def number_of_lines(filename=""):
    """Number of lines

    Args:
        filename (str): Name of the file. Defaults to "".

    Returns:
        int: amount of lines
    """
    with open(filename, "r", encoding="utf-8") as f:
        l = len(f.readlines())
    return l
