"""Mutating functions."""

__author__ = "730392828"


def manual_append(num_list: list[int], b: int) -> None:
    """docstring"""
    num_list.append(b)


a: list[int] = [1,2,3]
manual_append(a,2)

print(a)


def double(num_list2: list[int]) -> None:
    """docstring"""
    index = 0
    while index < len(num_list2):
        num_list2[index] *= 2
        index += 1


double(a)
print(a)