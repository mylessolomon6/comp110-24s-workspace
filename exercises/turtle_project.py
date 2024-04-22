"""Myles' forever-moving reconstruction."""

__author__ = "730392828"

from turtle import Turtle, colormode, done
colormode(255)

beetle: Turtle = Turtle()


def draw_tree(beetle: Turtle, x: float, y: float, branch_length: float) -> None:
    """Draw a square of the given width whose top-left corner is located at x, y."""
    beetle.penup()
    beetle.goto(x, y) 
    beetle.setheading(90.0)
    beetle.pendown()
    draw_branch(beetle, branch_length)


def draw_branch(beetle: Turtle, branch_length: float) -> None:
    """Making the branches of the tree."""
    if branch_length > 5:
        beetle.forward(branch_length)
        beetle.right(30)
        draw_branch(beetle, branch_length - 15)
        beetle.left(60)
        draw_branch(beetle, branch_length - 15)
        beetle.right(30)
        beetle.backward(branch_length)


def main() -> None:
    """The entrypoint of my scene."""
    my_turtle = Turtle()
    my_turtle.speed(0)  # Set the drawing speed to fastest
    my_turtle.color("brown")  # Set the color of the tree trunk
    draw_tree(my_turtle, 200, 0, 100)
    draw_tree(my_turtle, -50, 0, 120)
    draw_tree(my_turtle, 100, 0, 80)
    draw_tree(my_turtle, 250, 0, 100)
    done()


if __name__ == "__main__":
    main()
