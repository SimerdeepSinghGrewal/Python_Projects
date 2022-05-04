from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.up_right, "Up")
screen.onkeypress(r_paddle.down_right, "Down")
screen.onkeypress(l_paddle.up_left, "w")
screen.onkeypress(l_paddle.down_left, "s")
i = 1
game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(ball.max_speed)
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # detect bounce with paddle
    if ball.distance(r_paddle) <= 50 and ball.xcor() > 320:
        ball.bounce_x()
    elif ball.distance(l_paddle) <= 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect score
    if ball.xcor() > 400:
        score.increase_score(1)
        ball.new_game()
    elif ball.xcor() < -400:
        score.increase_score(0)
        ball.new_game()

screen.exitonclick()
