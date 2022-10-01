from turtle import Screen, Turtle
from snake import Snake
import time




screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

#the snake object
snake = Snake()

#this controls the snake
screen.listen()
screen.onkey(snake.moveUp, "Up")
screen.onkey(snake.moveDown, "Down")
screen.onkey(snake.moveLeft, "Left")
screen.onkey(snake.moveRight, "Right")





#this makes the snake automactically move forward
gameIsOn = True
while gameIsOn:
    #this updates the screen while the snake moves
    screen.update()
    time.sleep(0.1)
    
    snake.move()
        






screen.exitonclick()