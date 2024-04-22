"""Challenge Question...working to create a point."""

from __future__ import annotations


class Point:
    """Creating a class point."""

    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Defining a constructor."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Writing first method that belongs to Point, mutating it."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Returning a new point."""
        score: Point = Point(self.x * factor, self.y * factor)
        return score