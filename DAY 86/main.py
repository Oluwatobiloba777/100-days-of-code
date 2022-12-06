from blocks import Block
from turtle import *
from player import Player
from scoreboard import Scoreboard
from ball import Ball
import time

screen = Screen()
screen.setup(width=635, height=600)
bgcolor("black")
canvas = screen.getcanvas()
canvas.master.resizable(False, False)
screen.tracer(0)

ball = Ball()
block_manager = Block()
scoreboard = Scoreboard()
player = Player()

screen.listen()
screen.onkeypress(fun=player.left, key="q")
screen.onkeypress(fun=player.right, key="d")

block_manager.create_block()
scoreboard.refresh_score()
screen.update()

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    ball.move()
    screen.update()

    if ball.xcor() > 317.5 or ball.xcor() < -317.5:
        ball.bounce_x()

    if ball.ycor() < -300:
        ball.reset_position()

    if ball.ycor() > 300:
        ball.bounce_y()

    for block in block_manager.all_blocks:
        if ball.distance(block) < 20:
            block.ht()
            ball.bounce_y()
            if block.color() == ('yellow', 'yellow'):
                scoreboard.score += 1
            elif block.color() == ('green', 'green'):
                scoreboard.score += 3
            elif block.color() == ('orange', 'orange'):
                scoreboard.score += 5
            elif block.color() == ('red', 'red'):
                scoreboard.score += 7
            scoreboard.refresh_score()
            block_manager.all_blocks.remove(block)
            if block_manager.all_blocks == []:
                scoreboard.game_end()
                game_is_on = False
                screen.update()

    if ball.distance(player) < 40 and ball.ycor() >= -260:
        ball.bounce_y()

screen.mainloop()