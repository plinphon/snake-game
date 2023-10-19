from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.write("Score: 0", align="center", font=("Courier", 24, "normal"))
        self.score = 0
        self.highscore = 0
        self.score_position = (0,260)
        self.highscore_position = (0, 230)

    def write_score(self,point):
        if point > 0:
            self.score += 10
            self.clear()
            self.goto(self.score_position)
            self.write("Score: {}".format(self.score), align="center", font=("Courier", 24, "normal"))
            if self.score > self.highscore:
                self.highscore = self.score
            self.goto(self.highscore_position)
            self.write("high_score: {}".format(self.highscore), align="center", font=("Courier", 24, "normal"))
        else:
            self.clear()
            self.goto(self.score_position)
            self.write("GAME OVER!!", align="center", font=("Courier", 24, "normal"))
            self.goto(self.highscore_position)
            self.write("high_score: {}".format(self.highscore), align="center", font=("Courier", 24, "normal"))

    def reset(self):
        self.score = 0
        self.clear()
        self.goto(self.score_position)
        self.write("Score: 0", align="center", font=("Courier", 24, "normal"))
        self.goto(self.highscore_position)
        self.write("high_score: {}".format(self.highscore), align="center", font=("Courier", 24, "normal"))

   

