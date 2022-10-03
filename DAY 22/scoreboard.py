from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.Lscore = 0
        self.Rscore = 0
        self.updateScore()
        
    def updateScore(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.Lscore, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.Rscore, align="center", font=("Courier", 80, "normal"))

    def Lpoint(self):
        self.Lscore +=1
        self.updateScore()

    def Rpoint(self):
        self.Rscore +=1
        self.updateScore()