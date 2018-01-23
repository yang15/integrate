"""
This file contains the implementation of the Simpson rule
"""

import numpy as np


def evaluate(x, f):
    a = x[0]
    b = x[1]
    ya = f(a)
    yb = f((a + b) / 2.0)
    yc = f(b)
    I = (b - a) * (ya + 4.0 * yb + yc) / 6.0
    return I
