"""Splitting a dictionary into two lists."""

__author__ = "730392828"


def get_keys(y: dict[str, int]) -> list[str]:
    """Retreiving all the strings in a list."""
    x: list[str] = []
    for test in y:
        x.append(test)
    return x


def get_values(m: dict[str, int]) -> list[int]:
    """Retrieving all the values in the list."""
    k: list[int] = []
    for num in m:
        k.append(m[num])
    return k