"""Functions that implement sorting algorithms."""

__author__ = ""

def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm.
    Insert into an already sorted list."""
    idx = 0
    while idx < len(x) - 1:
        list_count = idx + 1
        while list_count > 0 and x[list_count] < x[list_count - 1]:
            b = x[list_count]
            x[list_count] = x[list_count - 1]
            x[list_count - 1] = b
            list_count -= 1
        idx += 1
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. 
    Repeatedly find the minimum and swap it."""
    idx = 0
    while idx < len(x):
        list_count = idx
        sec_count = list_count + 1
        while sec_count < len(x):
            if x[sec_count] < x[list_count]:
                list_count = sec_count
            sec_count += 1
        if list_count != idx:
            temp = x[list_count]
            x[list_count] = x[idx]
            x[idx] = temp
        idx += 1
    return None