#!/usr/bin/python3
"""THis module has a function to append text to a file
"""


def append_write(filename="", text=""):
    """Appends text to a file (or creates it if needed)

    Args:
        filename (str, optional): Filename. Defaults to "".
        text (str, optional): Content to append. Defaults to "".

    Returns:
        int: Amount of characters
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
