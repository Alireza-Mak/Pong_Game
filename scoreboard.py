from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")
FONT1 = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.p_r_score = 0
        self.p_l_score = 0
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 180)
        self.write(f"{self.p_l_score}  {self.p_r_score}", align=ALIGNMENT, font=FONT)

    def paddle_right_win(self):
        self.p_r_score += 1
        self.update_scoreboard()

    def paddle_left_win(self):
        self.p_l_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT1)
        self.goto(0, -50)
        if self.p_r_score == 10:
            winner = "Right"
        else:
            winner = "Left"
        self.write(f"{winner} player is winner", align=ALIGNMENT, font=FONT1)

    def check_game_status(self):
        self.update_scoreboard()
        if self.p_r_score == 10 or self.p_l_score == 10:
            self.game_over()
            return 10
        elif self.p_r_score > self.p_l_score:
            return self.p_r_score
        else:
            return self.p_l_score
