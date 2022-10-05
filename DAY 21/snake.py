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
        self.segments =[]
        self.createSnake()
        self.head = self.segments[0]

    #this creates the snake
    def createSnake(self):
        for positions in SNAKE_POSITIONS:
            self.addSegment(positions)
            

    #this requires the position to add the segment to
    def addSegment(self, positions):
        snakesSquares = Turtle("square")
        snakesSquares.color("white")
        snakesSquares.penup()
        snakesSquares.goto(positions)
        self.segments.append(snakesSquares)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.createSnake()
        self.head = self.segments[0]

    
    #this adds a new segment to the snake
    def extend(self):
        self.addSegment(self.segments[-1].position())


    def move(self):
        #this makes the snake squares move together
        for segNum in range(len(self.segments) -1, 0, -1):
            newX = self.segments[segNum -1].xcor()
            newY = self.segments[segNum -1].ycor()
            self.segments[segNum].goto(newX, newY)
        self.head.forward(MOVE_DISTANCE)

    def moveUp(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def moveDown(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def moveLeft(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def moveRight(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)