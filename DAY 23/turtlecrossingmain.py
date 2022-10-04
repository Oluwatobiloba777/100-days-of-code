from turtle import Screen
from turtleplayer import Player
from scoreboard import Scoreboard
from carmanager import CarManager
import time



screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
carManager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.goUp(), "Up")


gameIsOn = True
while gameIsOn:
    time.sleep(0.1)
    screen.update()

    carManager.createCar()
    carManager.moveCars()

    #detect collision with car
    for car in carManager.allCars:
        if car.distance(player) < 20:
            gameIsOn = False
            scoreboard.gameOver()

    #detect successful crossing
    if player.finish():
        player.start()
        carManager.levelUp()
        scoreboard.levelUp()


screen.exitonclick()