from turtle import *

x = 0
y = -260

STARTING_POSITION = (x, y)

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.shape("square")
        self.shapesize(stretch_len=0.5, stretch_wid=5)
        self.penup()
        self.color("white")
        self.goto(STARTING_POSITION)

    def left(self):
        x = self.xcor() - 20
        self.goto((x, y))

    def right(self):
        x = self.xcor() + 20
        self.goto((x, y))