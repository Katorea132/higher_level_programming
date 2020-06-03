#!/usr/bin/python3
"""This module constains a function that writes to a file
"""


def write_file(filename="", text=""):
    """This writes the contents of text to a file (overwrites if already
    exists)

    Args:
        filename (str, optional): Filename. Defaults to "".
        text (str, optional): COntent for the file. Defaults to "".

    Returns:
        int: characters written
    """
    with open(filename, "w", encoding="utf-8")as f:
        return f.write(text)
