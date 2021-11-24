import turtle
import random

class Ball(turtle.Turtle):

    def __init__(self, color):
        super().__init__()
        self.shape("circle")
        self.color(color)
        self.penup()
        self.x_move =  10
        self.y_move =  10
        self.ball_speed = 0.1

    # ball will move +10 on X and +10 on Y
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # if ball hits top wall or bottom wall, ball will bounce opposite direction
    def wall_bounce(self):
        self.y_move *= -1

    # if ball hits paddle, ball will bounce opposite direction
    def paddle_bounce(self):
        self.x_move *= -1
        self.ball_speed *= 0.9
        if self.x_move > 0:
            self.color("white") # can be blue to match hit
        else:
            self.color("white") # can be red to match hit

    # restarts the ball in center, with normal speed.
    def reset_ball_center(self):
        self.goto(0, 0) # sets ball back in center
        self.paddle_bounce() # changes ball start direction oppisite on each restart
        self.ball_speed = 0.1 # sets speed back to normal