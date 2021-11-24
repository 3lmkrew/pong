import turtle

class Paddle(turtle.Turtle): # inheriting from the Turtle() class

    def __init__(self, color, position): # pass the x, y position as a tuple ((-365, 0))
        super().__init__()  # must call super().__init__() when inheriting from another class
        self.shape("square") # shape of a box
        self.color(color) # color white to see inside black screen background color
        self.shapesize(5, 1) # turn the square into a rectangle
        self.penup() # lift pen to avoid drag lines
        self.goto(position) # Go to the position argument when call Paddle class

    # moves paddle object up
    def go_up(self):
        new_y = self.ycor() + 20 # when press "Up" arrow or "w" button, will move upwards by 20 steps per press
        self.goto(self.xcor(), new_y) # pass same x but new y coordinates

    # moves paddle object down
    def go_down(self):
        new_y = self.ycor() - 20 # when press "Down" arrow or "s" button, will move downwards by 20 steps per press
        self.goto(self.xcor(), new_y)