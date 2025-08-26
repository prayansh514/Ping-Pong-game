from turtle import Turtle,Screen
import random
import time
from paddle import *
from ball import *
from scoreboard import *

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.title("My ping pong game")
screen.setup (width=800, height=600)
screen.listen()


score = Scoreboard()
game_is_on = True
paddle_right = Paddle(350,0)
paddle_left = Paddle(-350,0)
screen.onkey(key="w", fun=paddle_left.up)
screen.onkey(key="s", fun=paddle_left.down)
screen.onkey(key="Up", fun=paddle_right.up)
screen.onkey(key = "Down",fun = paddle_right.down)

ball = Ball()



while game_is_on:
    screen.listen()
    screen.update()
    time.sleep(0.003)
    ball.move()

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    if ball.distance(paddle_right)<50 and ball.xcor()>340:
        ball.bounce_x()
    elif ball.xcor()>360:
        ball.goto(0,0)
        ball.direction_y = 1
        ball.direction_x = -1
        score.left_score = score.left_score + 1
        score.show()
        user = screen.textinput(title = "Ping Pong Game",prompt = "Do you want to continue? (Y/N)")
        if user=="N":
            game_is_on = False
            break
        else:
            paddle_left.goto(-350,0)
            paddle_right.goto(350,0)
            score.clear()
            screen.listen()


    if ball.distance(paddle_left)<50 and ball.xcor()<-340:
        ball.bounce_x()

    elif ball.xcor()<-360:
        ball.goto(0,0)
        ball.direction_y = 1
        ball.direction_x = 1
        score.right_score = score.right_score+1
        score.show()
        user = screen.textinput(title="Ping Pong Game", prompt="Do you want to continue? (Y/N)")
        if user == "N":
            game_is_on = False
            break
        else:
            paddle_left.goto(-350, 0)
            paddle_right.goto(350, 0)
            score.clear()
            screen.listen()






screen.exitonclick()