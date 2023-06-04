import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("pong")
screen.listen()

paddle1 = Paddle()
paddle2 = Paddle()
ball = Ball()

score1 = 0
score2 = 0
score_board = Turtle()
score_board.color("white")
score_board.penup()
score_board.goto(0, 250)
score_board.write(f'0 : 0', align="center", font=("Arial", 24, "normal"))
score_board.hideturtle()

screen.onkeypress(paddle1.up, "Up")
screen.onkeypress(paddle1.down, "Down")
screen.onkeypress(paddle2.wup, "w")
screen.onkeypress(paddle2.wdown, "s")

game = True

while game:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if paddle1.distance(ball) < 50 and ball.xcor() > 320:
        ball.hit()
    elif paddle2.distance(ball) < 50 and ball.xcor() < -320:
        ball.hit()

    if ball.xcor() > 400 or ball.xcor() < -400:

        if ball.xcor() > 400:
            score1 += 1
        elif ball.xcor() < -400:
            score2 += 1

        ball.refresh()
        paddle1.goto(350, 0)
        paddle2.goto(-350, 0)

        score_board.clear()
        score_board.write(f'{score1} : {score2}', align="center", font=("Arial", 24, "normal"))
        time.sleep(2)

screen.exitonclick()
