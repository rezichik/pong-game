
from turtle import Turtle

POSITIONS = [(350, 0), (-350, 0)]

class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.shapesize(1, 1)
        self.penup()
        self.right(45)
        self.xmove = 20
        self.ymove = 20

    def move(self):

        if self.ycor() + 20 >= 300 or self.ycor() - 20 <= -300:
            self.ymove *= -1

        newx = self.xcor() + self.xmove
        newy = self.ycor() + self.ymove
        self.goto(newx, newy)

    def hit(self):
        self.xmove *= -1

    def refresh(self):
        self.home()