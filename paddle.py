
from turtle import Turtle

POSITIONS = [(350, 0), (-350, 0)]

class Paddle(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.speed("fastest")
        self.penup()
        self.goto(POSITIONS[0])
        POSITIONS.remove(POSITIONS[0])

    def up(self):
        if(self.ycor() + 60 < 300):
            y = self.ycor() + 20
            self.goto(350, y)

    def down(self):
        if(self.ycor() - 60 > -300):
            y = self.ycor() - 20
            self.goto(350, y)

    def wup(self):
        if(self.ycor() + 60 < 300):
            y = self.ycor() + 20
            self.goto(-350, y)

    def wdown(self):
        if(self.ycor() - 60 > -300):
            y = self.ycor() - 20
            self.goto(-350, y)

