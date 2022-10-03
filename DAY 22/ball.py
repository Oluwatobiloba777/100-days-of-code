from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.Xmove = 3
        self.Ymove = 3
        self.moveSpeed = 0.1


    def move(self):
        newX = self.xcor() + self.Xmove
        newY = self.ycor() + self.Ymove
        self.goto(newX, newY)

    #this makes the ball bounce when it hits top and bottom which is the y-axis
    def Ybounce(self):
        self.Ymove *= -1


    #this makes the ball bounce when it hits top and bottom which is the x-axis
    def Xbounce(self):
        self.Xmove *= -1
        self.moveSpeed *= 0.9

    #this resets the position of the ball if it missed by the right paddle
    def resetPosition(self):
        self.goto(0,0)
        self.moveSpeed = 0.1
        self.Xbounce()