#!/usr/bin/python3
"""This is basically a way to multiply matrix
"""


def matrix_mul(m_a, m_b):
    """Multiplies matrix if possible

    Args:
        m_a (list of lists): Holds a list of lists (or else)
        m_b (list of lists): Holds a lists of lists (or else)

    Raises:
        TypeError: m_a or m_b are not a list
        TypeError: a member of m_a or m_b is not a list
        ValueError: m_a or m_b is empty
        TypeError: m_a or m_b members are not made only of integers or floats
        TypeError: The rows must all be of the same size
        ValueError: The matrix are not compatible to multiply

    Returns:
        list of lists: COntains the new matrix
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    elif type(m_b) is not list:
        raise TypeError("m_b must be a list")
    elif not all(type(x) is list for x in m_a):
        raise TypeError("m_a must be a list of lists")
    elif not all(type(x) is list for x in m_b):
        raise TypeError("m_b must be a list of lists")
    elif not m_a or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    elif not m_b or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    elif not all(all(type(y) in [float, int] for y in x) for x in m_a):
        raise TypeError("m_a should contain only integers or floats")
    elif not all(all(type(y) in [float, int] for y in x) for x in m_b):
        raise TypeError("m_b should contain only integers or floats")
    elif not all(len(x) is len(m_a[0]) for x in m_a):
        raise TypeError("each row of m_a must be of the same size")
    elif not all(len(x) is len(m_b[0]) for x in m_b):
        raise TypeError("each row of m_b must be of the same size")
    elif len(m_a[0]) is not len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    else:
        ret = [[] for x in m_a]

        for x in range(len(m_a)):
            for y in range(len(m_b[0])):
                a = 0
                for z in range(len(m_b)):
                    a += m_a[x][z] * m_b[z][y]
                ret[x].append(a)
        return ret
