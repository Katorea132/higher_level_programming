#!/usr/bin/python3
"""THe lazy way to multiply matrix
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """lazy matrix mult

    Returns:
        matrix: matrix
    """
    return numpy.matmul(m_a, m_b).tolist()
