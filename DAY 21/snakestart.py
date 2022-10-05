from turtle import Screen

from scoreboard import Scoreboard
from food import Food
from snake import Snake
import time




screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

#the snake object
snake = Snake()
#the food object
food = Food()
#the scoreboard object
scoreboard = Scoreboard()

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


    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increaseScore()

    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
        #print("Game Over")

    #detect collision with tail
    for segment in snake.segments[1:]:#with slicing
        #without slicing -[1:] use this code below and change second if to elif
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
        


screen.exitonclick()