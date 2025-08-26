from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0,200)
        self.left_score = 0
        self.right_score = 0


    def show(self):
        self.clear()
        self.write(f"Left player Score is {self.left_score} | Right player score is {self.right_score}", move=False,
                   align="center", font=('Arial', 18, 'normal'))