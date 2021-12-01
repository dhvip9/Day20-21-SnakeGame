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
        self.high_score = ""
        self.score_body()

    def score_body(self):
        """Set Score Body"""
        self.clear()
        with open("highscore.txt") as save_high_score:
            self.high_score = save_high_score.read()
        self.write(arg=f"[ Score : {self.score}  HighScore : {self.high_score}]", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Set Scoreboard Increase"""
        self.score += 1
        self.score_body()

    def reset(self):
        if self.score > int(self.high_score):
            with open("highscore.txt", mode="w") as save_high_score:
                save_high_score.write(str(self.score))
        self.score = 0
        self.score_body()

    def game_over(self):
        """Set GameOver Message"""
        self.home()
        self.write(arg="GameOver!", align=ALIGNMENT, font=FONT)


