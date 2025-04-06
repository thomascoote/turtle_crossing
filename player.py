from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(0,-370)

    def move_forward(self):
        self.goto(self.xcor(), self.ycor()+40)