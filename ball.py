from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.setheading(180)
        self.xmove = 10
        self.ymove = 10
        self.movespeed = 0.1

    def change_direction(self):
        x = self.heading()
        self.setheading(x + 90)

    def move(self):
        self.goto(self.xcor() + self.xmove, self.ycor() + self.ymove)

    def bounce(self):
        self.ymove *= -1

    def backbounce(self):
        self.xmove *= -1
        self.movespeed *= 0.9

    def reset_position(self):
        self.xmove *= -1
        self.goto(0, 0)
        self.movespeed = 0.1
