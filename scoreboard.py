from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.score = 0
        self.write(self.score, align = "center", font = ("minecraft", 30, "bold"))

    def increase(self):
        self.score += 1
        self.clear()
        self.write(self.score, align="center", font=("minecraft", 30, "bold"))


