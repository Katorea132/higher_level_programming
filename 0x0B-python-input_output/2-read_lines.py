#!/usr/bin/python3
"""This module reads n amount of lines
"""


def read_lines(filename="", nb_lines=0):
    """Reads N lines

    Args:
        filename (str, optional): Filename. Defaults to "".
        nb_lines (int, optional): Amount of lines. Defaults to 0.
    """
    with open(filename, "r", encoding="utf-8") as f:
        if nb_lines < 1:
            print(f.read(), end="")
            return
        for __ in range(nb_lines):
            print(f.readline())
