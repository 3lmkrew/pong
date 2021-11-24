import turtle

class ScoreBoard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    # Updates score board with new score
    def update_score(self):
        self.clear()
        self.goto(-100, 230)
        self.write(self.l_score, align="center", font=("Courier", 50, "normal"))
        self.goto(-100, 225)
        self.write("|__|", align="center", font=("Courier", 25, "normal"))
        self.goto(100, 230)
        self.write(self.r_score, align="center", font=("Courier", 50, "normal"))
        self.goto(100, 225)
        self.write("|__|", align="center", font=("Courier", 25, "normal"))
        self.goto(0, 0)
        for y_axis in range(-500, 500, 40): # create a dashed line in the center of game
            self.goto(0, y_axis)
            self.write("|" , align="center", font=("Courier", 25, "normal"))

    # adds point to left side and updates score
    def left_point(self):
        self.l_score += 1
        self.update_score()

    # adds point to right side and updates score
    def right_point(self):
        self.r_score += 1
        self.update_score()