"""Our Fourth Assignment for CompSci110."""

__author__ = "730392828"


def all(numl: list[int], reg: int) -> bool:
    """Defining all."""
    if len(numl) == 0:
        return False
    num_counter = 0
    while num_counter < len(numl):
        if numl[num_counter] != reg:
            return False
        num_counter += 1
    return True


def max(input: list[int]) -> int:
    """Returning the highest integer from a list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    index = 0
    max_num = input[0]
    while index < len(input):
        if input[index] > max_num:
            max_num = input[index]
        index += 1
    return max_num


def is_equal(g: list[int], h: list[int]) -> bool:
    """Defining is_equal for if a pair of list is identical."""
    num_counter = 0
    while num_counter < len(g) and num_counter < len(h):
        if len(g) != len(h):
            return False
        elif g[num_counter] != h[num_counter]:
            return False
        num_counter += 1
    return True


def extend(a: list[int], b: list[int]) -> None:
    """Defining extend function to add one list to another."""
    a += b