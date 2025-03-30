from turtle import Screen
from bar import Bar
from ball import Ball
from scoreboard import Scoreboard
import time

size = 20
WIDTH = 800
BORDER = 2 * 2
CHROME = 9 * 4
HEIGHT = 600

screen = Screen()
screen.screensize(800, 600)
screen.listen()
screen.bgcolor("black")
screen.tracer(0)
screen.title("Retro Pong")

bar1 = Bar(size / 2 - WIDTH / 2 + (BORDER * 8), 0)
bar2 = Bar(WIDTH / 2 - size / 2 - BORDER - CHROME, 0)
bars = [bar1, bar2]
ball = Ball()
bar1_s = Scoreboard(-50, 250)
bar2_s = Scoreboard(50, 250)
pos = -300
for i in range(10):
    partition = Bar(0, pos, wid = 3, ln = 0.5)
    pos += 100

screen.onkeypress(bar2.move_f, "Up")
screen.onkeypress(bar2.move_b, "Down")
screen.onkeypress(bar1.move_f, "w")
screen.onkeypress(bar1.move_b, "s")
screen.onkeypress(screen.bye, "e")

while True:
    time.sleep(ball.movespeed)
    ball.move()
    screen.update()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(bar2) < 50 and ball.xcor() > 320 or ball.distance(bar1) < 50 and ball.xcor() < -320:
        ball.backbounce()

    if ball.xcor() > 370:
        ball.reset_position()
        bar1_s.increase()

    if ball.xcor() < -370:
        ball.reset_position()
        bar2_s.increase()
