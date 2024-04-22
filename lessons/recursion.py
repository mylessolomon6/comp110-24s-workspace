"""Learning recursion."""

__author__ = "730392828"


def f(n: int, k: int) -> int:
    """Defining f."""
    if n == 0:  # base case
        return 0
    else:  # recursion case
        return f(n - 1, k) + k