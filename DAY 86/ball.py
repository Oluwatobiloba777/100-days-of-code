from turtle import *

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.xmove = 4
        self.ymove = 4
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto((new_x, new_y))

    def bounce_x(self):
        self.xmove *= -1

    def bounce_y(self):
        self.ymove *= -1

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()