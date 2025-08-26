from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(0)
        self.direction_x = 1
        self.direction_y = 1

    def move(self):
        new_x = self.xcor()+1*self.direction_x
        new_y = self.ycor()+1*self.direction_y
        self.goto(new_x,new_y)

    def bounce_x(self):
        self.direction_x = self.direction_x * -1

    def bounce_y(self):
        self.direction_y = self.direction_y * -1

