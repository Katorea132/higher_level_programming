#!/usr/bin/python3
"""THe lazy way to multiply matrix
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """A lazy way of multiplying matrix

    Args:
        m_a (list of lists): [description]
        m_b (list of lists): [description]

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
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    elif not all(type(x) is list for x in m_b):
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    elif not m_a or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    elif not m_b or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    elif not all(all(type(y) in [float, int] for y in x) for x in m_a):
        raise TypeError("invalid data type for einsum")
    elif not all(all(type(y) in [float, int] for y in x) for x in m_b):
        raise TypeError("invalid data type for einsum")
    elif not all(len(x) is len(m_a[0]) for x in m_a):
        raise TypeError("setting an array element with a sequence.")
    elif not all(len(x) is len(m_b[0]) for x in m_b):
        raise TypeError("setting an array element with a sequence.")
    elif len(m_a[0]) is not len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    else:
        return numpy.matmul(m_a, m_b).tolist()
