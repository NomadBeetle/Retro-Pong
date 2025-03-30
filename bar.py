from turtle import Turtle

class Bar(Turtle):
    def __init__(self, x, y, wid = 5, ln = 1):
        super().__init__()
        self.shape("square")
        # self.setheading(90)
        self.penup()
        self.color("white")
        self.speed("fast")
        self.turtlesize(stretch_wid = wid, stretch_len = ln)
        self.goto(x, y)


    def move_f(self):
        if self.ycor() <= 260:
            self.goto(self.xcor(), self.ycor() + 20)

    def move_b(self):
        if self.ycor() >= -260:
            self.goto(self.xcor(), self.ycor() - 20)

    def auto(self):
        x = self.heading()
        if self.ycor() >= 260 or self.ycor() <= -260:
            self.setheading(x + 180)
        self.fd(20)