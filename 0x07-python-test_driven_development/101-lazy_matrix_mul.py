#!/usr/bin/python3.5
"""A function that multiplies 2 matrices"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Function that multiplies 2 matrices

    Args:
        m_a: matrix a
        m_b: matrix b

    Returns:
        Result of the multiplication
    """
    return (np.matmul(m_a, m_b))
