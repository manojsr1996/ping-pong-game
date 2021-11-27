from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)
screen.listen()


r_paddle = Paddle()
r_paddle.goto(370, 0)
screen.onkey(r_paddle.move_up, 'Up')
screen.onkey(r_paddle.move_down, 'Down')
l_paddle = Paddle()
l_paddle.goto(-370, 0)
screen.onkey(l_paddle.move_up, 'w')
screen.onkey(l_paddle.move_down, 's')

ball = Ball()
score = Score()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_move()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 355 or ball.distance(l_paddle) < 50 and ball.xcor() < -355:
        ball.x_move()

    if ball.xcor() > 370:
        ball.opposite()

    if ball.xcor() < -370:
        ball.opposite()


screen.exitonclick()





