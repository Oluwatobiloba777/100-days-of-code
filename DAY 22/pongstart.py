from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
#this turns off the animation
screen.tracer(0)

#objects
Rpaddle = Paddle((350, 0))
Lpaddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()




screen.listen()
screen.onkey(Rpaddle.goUp, "Up")
screen.onkey(Rpaddle.goDown, "Down")
screen.onkey(Lpaddle.goUp, "w")
screen.onkey(Lpaddle.goDown, "x")

#this will keep the animation on and move it to the right when it refreshes
gameIsOn = True
while gameIsOn:
    time.sleep(ball.moveSpeed)
    screen.update()
    ball.move()


    #detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #this calls the ball bounce method
        ball.Ybounce()

    #detect collision with right paddle and left paddle
    if ball.distance(Rpaddle) < 50 and ball.xcor() > 320 or ball.distance(Lpaddle) < 50 and ball.xcor() < -320:
        ball.Xbounce()

    #detect if right paddle misses the ball
    if ball.xcor() > 380:
        ball.resetPosition()
        scoreboard.Lpoint()

    #detect if left paddle misses the ball
    if ball.xcor() < -380:
        ball.resetPosition()
        scoreboard.Rpoint

screen.exitonclick()