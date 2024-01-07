import io
from turtle import Turtle
FONT = ("Courier", 15, 'bold')
ALIGNMENT = "center"


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.score = 0
        with open("data.txt", "w") as high_score:
            try:
                self.high_score = int(high_score.read())
            except io.UnsupportedOperation:
                self.high_score = 0
        self.penup()
        self.setposition(0, 275)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"SCORE: {self.score} High Score: {self.high_score}", False, ALIGNMENT, font=FONT)

    def write_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def reset_score(self):
        self.setposition(0, 275)
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.score = 0
        self.update_scoreboard()

    def write_high_score(self):
        with open("data.txt", mode="w") as high_score:
            score = str(self.score)
            high_score.write(score)

    def pause(self):
        self.clear()
        self.setposition(0, 0)
        self.write("PAUSED", False, ALIGNMENT, font=("Courier", 30, 'bold'))

    def resume(self):
        self.setposition(0, 275)
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.setposition(0, 30)
        self.write("GAME OVER", False, ALIGNMENT, font=("Courier", 30, 'bold'))
        self.setposition(0, 0)
        self.write(f"SCORE: {self.score}", False, ALIGNMENT, font=FONT)
        self.setposition(0, -30)
        self.write("Press 'Space Bar' to Restart", False, ALIGNMENT, font=("Courier", 12, 'bold'))

    def reset_high_score(self):
        with open("data.txt", mode="w") as high_score:
            self.score = 0
            score = str(self.score)
            high_score.write(score)
