# By: 3lmkrew
# Date: 06/03/2021

import turtle
import time
from paddle import Paddle
from pong_ball import Ball
from score_board import ScoreBoard

# create the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Mason's Pong Game")
screen.tracer(0)

# Create two Paddle objects
left_paddle = Paddle("blue", (-350, 0))  # creates left paddle object, pass paddle color and (x, y) location
right_paddle = Paddle("red", (350, 0))  # creates right paddle object, pass paddle color and (x, y) location

# Create a Ball object
ball = Ball("white")

# Create a ScoreBoard object
score_board = ScoreBoard()

# call listen() method to be able to use keyboard keys.
screen.listen()  # must call first to activate onkey() buttons, pass screen object
screen.onkey(left_paddle.go_up, "w")  # left paddle move UP by pressing 'w'
screen.onkey(left_paddle.go_down, "s")  # left paddle move DOWN by pressing 's'
screen.onkey(right_paddle.go_up, "Up")  # right paddle move UP by pressing 'Up arrow'
screen.onkey(right_paddle.go_down, "Down")  # right paddle move DOWN by pressing 'Down arrow'

game_on = True  # switch for loop

while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    # if the ball hits top or bottom it will bounce off the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    # if the ball hits the paddle, it will bounce to opposite side
    if ball.distance(right_paddle) < 60 and ball.xcor() > 325 or ball.distance(left_paddle) < 60 and ball.xcor() < -325:
        ball.paddle_bounce()

    # if right paddle misses ball, left gets point.
    if ball.xcor() > 380:
        score_board.left_point()
        ball.reset_ball_center()

    # if left paddle misses ball, right gets point
    if ball.xcor() < -380:
        score_board.right_point()
        ball.reset_ball_center()


screen.exitonclick()
