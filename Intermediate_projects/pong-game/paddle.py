from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def up_left(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down_left(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def up_right(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down_right(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
