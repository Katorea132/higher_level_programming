#!/usr/bin/python3
"""THis module makes a pascal's triangle
"""


def pascal_triangle(n):
    """PAscal solution

    Args:
        n (lenght): lenght of pascal

    Returns:
        list: list of lists of integers
    """
    if n <= 0:
        return []
    list = []
    for y in range(n):
        list.append([1])
        if y > 1:
            for x in range(y - 1):
                list[y].append(list[y - 1][x] + list[y - 1][x + 1])
        if y is not 0:
            list[y].append(1)
    return list
