"""Summing the elements of a list using different loops"""

__author__ = "730392828"

def w_sum(vals: list[float]) -> float:
    """Defining the variable w_sum."""
    idx = 0
    while idx < len (vals):
        print (vals[idx])
        idx += 1


def f_sum(vals: list[float]) -> float:
    """Defining the variable f_sum."""
    idx = 0
    for ghost in vals:
        idx += ghost
    return idx


def f_range_sum(vals: list[float]) -> float:
    """Defining the variable f_range_sum."""
    idx = 0
    for car in range(len(vals)):
        idx += vals[car]
    return idx
