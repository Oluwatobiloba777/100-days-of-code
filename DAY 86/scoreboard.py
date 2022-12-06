from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-0, 260)
        self.score = 0

    def refresh_score(self):
        self.clear()
        self.color("white")
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))

    def game_end(self):
        self.goto(0,0)
        self.write(f"YOU WON WITH {self.score} points !", align="center",font=("Courier", 24, "normal"))
