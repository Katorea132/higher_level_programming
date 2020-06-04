#!/usr/bin/python3
"""THis appends a text file when a string is found
"""


def append_after(filename="", search_string="", new_string=""):
    """Writes the new text

    Args:
        filename (str, optional): filename. Defaults to "".
        search_string (str, optional): string to search for. Defaults to "".
        new_string (str, optional): string to put. Defaults to "".
    """
    with open(filename, mode="r+", encoding="uft-8") as f:
        for line in f:
            new += line
            if search_string in line:
                new += new_string
        f.write(new)
