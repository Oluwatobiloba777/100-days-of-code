from turtle import Turtle, Screen
import random


isRaceOn = False
screen = Screen()
screen.setup(width=500, height=400)
userInput = screen.textinput(title="Make your bet", prompt="Which turle will win the race? Enter a color: ")
colors = ["red","orange","yellow","green","blue","purple"]
yPostions = [-60,-20,20,60,100,140]
allTurtles = []

for turtles in range(0,6):
    newTurtle = Turtle(shape="turtle")
    newTurtle.color(colors[turtles])
    newTurtle.penup()
    newTurtle.goto(x=-240, y=yPostions[turtles])
    allTurtles.append(newTurtle)

if userInput:
    isRaceOn = True



while isRaceOn:
    for turtle in allTurtles:
        if turtle.xcor() > 230:
            isRaceOn = False
            winningColor = turtle.pencolor()
            if winningColor == userInput:
                print(f"You have won! The {winningColor} turtle is the winner!")
            else:
                print(f"You have lost! The {winningColor} turtle is the winner!")
        distance = random.randint(0,10)
        turtle.forward(distance)


screen.exitonclick()