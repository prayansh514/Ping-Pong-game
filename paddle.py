from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.position(x,y)
        self.setheading(90)



    def position(self,x,y):
        self.goto(x,y)

    def up(self):
        if self.ycor()<190:
            self.forward(30)

    def down(self):
        if self.ycor()>-190:
            self.backward(30)
