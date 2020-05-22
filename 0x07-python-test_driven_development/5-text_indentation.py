#!/usr/bin/python3
""" THis is a function that adds 2 new lines after
every ".:?"
"""


def text_indentation(text):
    """Prints a text separating with 2 newlines every .:?
    encountered

    Args:
        text (str): Holds the string -Must be a string- to separate

    Raises:
        TypeError: In case text is not a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for c in ".:?":
        text = (c + "\n\n").join([w.strip(" ") for w in text.split(c)])
    print(text, end="")
