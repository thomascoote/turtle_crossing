from turtle import Turtle

class Score:
    def __init__(self):
        self.score_draw = Turtle()
        self.left_score = 0
        self.start_score()
        self.score_draw.hideturtle()

    def write_score(self):
        self.score_draw.write(arg=f"Score:{self.left_score}", font=("Arial", 20, "normal"))

    def start_score(self):
        #Start left score
        self.score_draw.penup()
        self.score_draw.goto(-350,370)
        self.score_draw.pendown()
        self.write_score()
        self.score_draw.penup()

    def add_score(self):
        self.left_score += 1
        self.score_draw.clear()
        self.write_score()