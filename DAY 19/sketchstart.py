from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def moveUp():
    tim.forward(10)


def moveDown():
    tim.backward(10)


def moveLeft():
    tim.left(10)


def moveRight():
    tim.right(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="Up", fun=moveUp)
screen.onkey(key="Down", fun=moveDown)
screen.onkey(key="Left", fun=moveLeft)
screen.onkey(key="Right", fun=moveRight)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
