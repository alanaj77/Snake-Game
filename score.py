from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_val = 0
        self.penup()
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.goto(0,250)
        self.color("white")
        self.goto(0, 275)
        self.write("High Score = ", True, "center",font=("arial",15,"bold"))
        with open("data.txt") as data:
            high_score = data.read()
            self.write(high_score, True,font=("arial",15,"bold"))
    def update_score(self):
        self.clear()
        self.score_val += 1
        self.goto(0, 250)

        self.write("Score = ",True,"center",font=("arial",15,"bold"))
        self.write( self.score_val, True,font=("arial",15,"bold"))


    def game_over(self):
        print(f"{self.high_score},{self.score_val}")
        if self.high_score < self.score_val:
            self.high_score = self.score_val
            print(self.high_score)
            with open("data.txt",mode = "w+") as data:

                print("hello")
                high_score = str(self.high_score)
                data.write(high_score)

        self.goto(0,0)
        self.color("White")
        self.write("Game Over", True, "center",font=("arial",30,"bold"))