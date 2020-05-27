#!/usr/bin/python3
"""THe lazy way to multiply matrix
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """lazy matrix multiplication

    Returns:
        matrix: matrix
    """
    return numpy.matrix(m_a) * numpy.matrix(m_b)
