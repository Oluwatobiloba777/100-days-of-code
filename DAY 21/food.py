from turtle import Turtle
import random


class Food(Turtle):
    #inheriting from the turtle class
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
        
    #this refreshes food each time the snake head collides with food
    def refresh(self):
        randomX = random.randint(-280,280)
        randomY = random.randint(-280,280)
        self.goto(randomX, randomY)