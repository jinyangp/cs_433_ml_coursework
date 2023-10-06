# -*- coding: utf-8 -*-
"""implement a polynomial basis function."""

import numpy as np


def build_poly(x, degree):
    """polynomial basis functions for input data x, for j=0 up to j=degree."""
    # ***************************************************
    # INSERT YOUR CODE HERE
    # polynomial basis function: TODO
    # this function should return the matrix formed
    # by applying the polynomial basis to the input data

    res = np.empty((x.shape[0], degree + 1), dtype = np.float64)
    for d in range(degree + 1):
        res[:, d] = np.apply_along_axis(lambda s: s**d, 0, x)
        
    return res
    # ***************************************************
