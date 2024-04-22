"""Learning about the turtle. """

from turtle import Turtle, colormode, done
colormode(255)

leo: Turtle = Turtle()

leo.speed(50)
leo.hideturtle()


leo.begin_fill()
# to turn the turtle off and prevent from drawing unwanted line. 
leo.penup()
leo.goto(-120, -90)
leo.pendown()
leo.color(255, 51, 120)
leo.fillcolor(32, 67, 93)
# converting it into a triangle. 
i: int = 0
while i < 3:
    leo.forward(300)
    leo.left(120)
    i += 1
leo.end_fill()



bob: Turtle = Turtle()

bob.color(18, 2, 2)
bob.penup()
bob.goto(45, 60)
bob.pendown()
i: int = 0
side_length: int = 300
while (i < 3):
    bob.forward(side_length)
    bob.left(120)
    i = i + 1
    
done()