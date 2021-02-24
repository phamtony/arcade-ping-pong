from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 40, "normal")
PLAYER_ONE_CORD = (-100, 200)
PLAYER_TWO_CORD = (100, 200)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.score_board_update()

    def l_point(self):
        self.l_score += 1
        self.score_board_update()

    def r_point(self):
        self.r_score += 1
        self.score_board_update()

    def score_board_update(self):
        self.clear()
        self.goto(PLAYER_ONE_CORD)
        self.write(f"{self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto(PLAYER_TWO_CORD)
        self.write(f"{self.r_score}", align=ALIGNMENT, font=FONT)
