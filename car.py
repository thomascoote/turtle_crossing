from random import randrange
from turtle import Turtle
import random

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.speed = random.randrange(1,3)
        self.start = random.randrange(350,800)
        self.penup()
        self.pen(fillcolor="black",pencolor="black")
        self.shape("square")
        self.shapesize(1,2)
        self.goto(self.start,200)
        self.car_colour()

    def car_colour(self):
        r_random = randrange(5,240)
        g_random = randrange(5,240)
        b_random = randrange(5,240)

        colour_tup = (r_random,g_random,b_random)
        self.pen(fillcolor=colour_tup,pencolor=colour_tup)

    def car_left(self):
        x_pos = self.xcor()
        y_pos = self.ycor()
        self.goto(x_pos-self.speed,y_pos)