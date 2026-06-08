from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_val = 0
        self.penup()
        self.hideturtle()
        self.goto(0,280)
        self.color("white")
        self.write("Score = ",True,"center")
        self.write( self.score_val, True)
    def update_score(self):
        self.clear()
        self.score_val += 1
        self.goto(0, 280)
        self.write("Score = ",True,"center")
        self.write( self.score_val, True)

    def game_over(self):
        self.clear()
        self.color("White")
        self.write("Game Over", True, "center")