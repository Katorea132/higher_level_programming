#!/usr/bin/python3
def remove_char_at(str, n):
    '''
    First attempt at a docstring: This function removes a character of a string
    in a given index'''
    for c in str:
        if (n >= 0):
            return str[:n] + str[n + 1:]
        else:
            return str
