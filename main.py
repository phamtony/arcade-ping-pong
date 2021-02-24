from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
game_ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(game_ball.move_speed)
    screen.update()
    game_ball.move()

    # detect collision
    if game_ball.ycor() > 280 or game_ball.ycor() < -280:
        #needs to bounce
        game_ball.bounce_y()

    # detect paddle collision
    if game_ball.distance(r_paddle) < 50 and game_ball.xcor() > 320 or game_ball.distance(l_paddle) < 50 and game_ball.xcor() < -320:
        game_ball.bounce_x()

    if game_ball.xcor() > 380:
        game_ball.reset_position()
        scoreboard.l_point()

    if game_ball.xcor() < -380:
        game_ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
