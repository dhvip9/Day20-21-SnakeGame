from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.setposition(x=0.00, y=270)
        self.score = 0
        self.score_body()

    def score_body(self):
        """Set Score Body"""
        self.write(arg=f"[ Score : {self.score} ]", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Set Scoreboard Increase"""
        self.score += 1
        self.score_body()

    def game_over(self):
        """Set GameOver Message"""
        self.home()
        self.write(arg="GAME OVER!", align=ALIGNMENT, font=FONT)
