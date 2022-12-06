from turtle import *

COLORS = ['red', 'orange', 'green', 'yellow']

class Block(Turtle):
    def __init__(self):
        self.all_blocks = []

    def new_block(self, x, y, color):
        new_block = Turtle("square")
        new_block.penup()
        new_block.goto(x, y)
        new_block.shapesize(stretch_len=2, stretch_wid=0.5)
        new_block.color(color)
        self.all_blocks.append(new_block)

    def create_block(self):
        x = 277
        y = 200
        color = 0
        for i in range(4):
            while x > -300:
                self.new_block(x, y, COLORS[color])
                x -= 47
            y -=15
            x = 277
            color +=1