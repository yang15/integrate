"""
This file contains the implementation of the Simpson rule
"""

import numpy as np


def evaluate(bounds, func):
    """

    Evaluates simpsons rules on an array of values and a function pointer.
    \int_{a}^{b} = \int ...

    Parameters
    ----------
    bounds : array_like
        An array with a dimension of two that contains the starting and ending points of the integrand.
    fund : function
        Evalute the integrand at a series of points.

    Returns
    -------
    integral : float
        The integral of the function between the bounds.

    """
    if len(bounds) != 2:
        raise ValueError("Bounds should be a length of two, found %d." % len(bounds))

    a = bounds[0]
    b = bounds[1]
    ya = func(a)
    yb = func((a + b) / 2.0)
    yc = func(b)
    I = (b - a) * (ya + 4.0 * yb + yc) / 6.0
    return I
