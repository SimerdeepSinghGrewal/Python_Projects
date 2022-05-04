from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"{self.l_score} : {self.r_score}", align="center", font=("Arial", 20, "normal"))
        self.ht()

    def increase_score(self, scr):
        if scr == 1:
            self.l_score += 1
            self.clear()
            self.write(f"{self.l_score} : {self.r_score}", align="center", font=("Arial", 20, "normal"))
        elif scr == 0:
            self.r_score += 1
            self.clear()
            self.write(f"{self.l_score} : {self.r_score}", align="center", font=("Arial", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 28, "normal"))
