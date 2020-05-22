#!/usr/bin/python3
"""
This will print names, like Isaac Shredder and
Willy Wonka, maybe even Walter White, if you happen to be
god damn right
"""


def say_my_name(first_name, last_name=""):
    """This function will print the name of the person, or
    the lines associated with the character :D

    Args:
        first_name (str): First name
        last_name (str): Last name. Defaults to "".

    Raises:
        TypeError: In case either first or last name aren't strings
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    if first_name is "General" and last_name is "Kenobi":
        print("Hello there")
        return
    if first_name is "General" and last_name is "Grevous":
        print("General Kenobi")
        return
    print("My name is {} {}".format(first_name, last_name))
