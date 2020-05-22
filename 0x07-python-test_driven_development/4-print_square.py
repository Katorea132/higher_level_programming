#!/usr/bin/python3
""" This module contains a function to print squares :D
"""


def print_square(size):
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    r = range(size)
    print("\n".join(["".join(["#" for x in r]) for y in r]))
