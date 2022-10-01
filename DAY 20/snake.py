from turtle import Turtle

#this gives the snake three squares positions length before increment
SNAKE_POSITIONS = [(0,0), (-20,0),(-40,0)]

#this makes the snake move forward
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segements =[]
        self.createSnake()

    def createSnake(self):
        for positions in SNAKE_POSITIONS:
            snakesSquares = Turtle("square")
            snakesSquares.color("white")
            snakesSquares.penup()
            snakesSquares.goto(positions)
            self.segements.append(snakesSquares)

    def move(self):
        #this makes the snake squares move together
        for segNum in range(len(self.segements) -1, 0, -1):
            newX = self.segements[segNum - 1].xcor()
            newY = self.segements[segNum - 1].ycor()
            self.segements[segNum].goto(newX, newY)
        self.segements[0].forward(MOVE_DISTANCE)

    def moveUp(self):
        if self.segements[0].heading() != DOWN:
            self.segements[0].setheading(UP)

    def moveDown(self):
        if self.segements[0].heading() != UP:
            self.segements[0].setheading(DOWN)

    def moveLeft(self):
        if self.segements[0].heading() != RIGHT:
            self.segements[0].setheading(LEFT)

    def moveRight(self):
        if self.segements[0].heading() != LEFT:
            self.segements[0].setheading(RIGHT)