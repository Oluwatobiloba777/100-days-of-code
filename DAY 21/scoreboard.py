from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    #inheriting from the trutle class
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.updateScoreboard()
        
    def updateScoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
   
    
    def gameOver(self):
        self.goto(0, 0)
        self.write("GAME OVER YOU PUSSY!!!", align=ALIGNMENT, font=FONT)
    
    def increaseScore(self):
        self.score +=1
        self.clear()
        self.updateScoreboard()