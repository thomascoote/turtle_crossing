from turtle import Turtle, Screen

from player import Player
from car import Car
from score import Score
import random

# 1 - 800x800 screen

# 2 - Turtle at bottom of screen. can only move forward with a key press

# 3 - Cars of different colours (and speeds?) pass the screen from right to left.

# 4 - Collision detection for car hitting turtle. If hit, game over.

# 5 - Win screen for reaching the other side of the road

# 6 - Scoreboard, and increase speed of cars with each successful game.


#Screen setup
screen = Screen()
screen_width = 800
screen_height = 800
screen.setup(width=screen_width,height=screen_height,startx=400,starty=1)
screen.title("Frogger")
screen.colormode(cmode=255)
screen.tracer(0)
screen.listen()

scoreboard = Score()

#Player Character
char=Player()

#Game Parameters
car_amount = 18
space_between_cars = 40

#Cars
car_list = []
car_class_list = []
car_starting_locations = []
back_car = []

#Road Drawing
starting_position = (-400,-350)
road = Turtle()
road.pen(pencolor="black",fillcolor="black",pensize=2)
road.penup()
road.goto(starting_position)
road.pendown()

for i in range (0,car_amount):
    road.goto(x=800,y=road.ycor())
    road.goto(x=800,y=road.ycor()+space_between_cars)
    road.goto(x=-800,y=road.ycor())
    road.goto(x=-800,y=road.ycor()+space_between_cars)

#Dash Markings
dash_start = (-400, -330)
dash = Turtle()
dash.pen(pencolor="black",fillcolor="black",pensize=1)
dash.penup()
dash.goto(dash_start)
dash.pendown()

for i in range (0,car_amount+1):
    while dash.xcor() < 800:
        dash.goto(dash.xcor()+20,dash.ycor())
        dash.pendown()
        dash.goto(dash.xcor()+20,dash.ycor())
        dash.penup()
    dash.goto(x=dash_start[0],y=dash_start[1]+(i*space_between_cars))

#Set car starting locations
for i in range(0, car_amount):
    offset_x = random.randrange(350,800)
    offset_y = i * space_between_cars
    car_location = (offset_x,(350 - offset_y))
    car_starting_locations.append(car_location)

#Append car_names to car_list
for i in range(0,car_amount):
    car_name = f"car{i}"
    car_list.append(car_name)

#Append Car Class objects to car_class_list
for i in car_list:
    i = Car()
    car_class_list.append(i)

#Spawns the initial cars with a random X value
for i in car_class_list:
    starting_loc = random.choice(car_starting_locations)
    i.goto(starting_loc)
    car_starting_locations.remove(starting_loc)
    back_car.append(i)

def screen_update():
    screen.update()

def move_forward():
    char.move_forward()

def car_move():
    for i in car_class_list:
        i.car_left()

def add_car_to_lane(turtle_object):
    new_car = Car()
    y = turtle_object.ycor()
    offset_x = 400
    car_class_list.append(new_car)
    new_car.goto(offset_x,y)
    back_car.append(new_car)

def increase_score():
    scoreboard.add_score()
    char.goto(x=0,y=-370)
    for i in car_class_list:
        i.increase_speed()

def game_over():
    draw = Turtle()
    draw.pen(pensize=20)
    screen.clear()
    draw.write("GAME OVER",align="center",font=("Arial",20,"normal"))

#Keybinds
screen.onkeypress(fun=move_forward,key="w")

game_run = True
ready = False
while game_run:
    #Starts drawing screen when the first car reaches 0 on the X axis (center of the screen)
    while not ready:
        car_move()
        for i in car_class_list:
            if i.xcor() < 0:
                ready = True

    #Main Loop
    update=screen_update()
    screen.ontimer(fun=update, t=50)
    car_move()

    #Add car to lane
    for i in back_car:

        if i.xcor() < random.randrange(0,100):
            back_car.remove(i)
            add_car_to_lane(i)

    #Check for collisions
    for i in car_class_list:
        if i.xcor()-20 < char.xcor() < i.xcor()+20 and i.ycor()-10 < char.ycor() < i.ycor()+10:
            screen.clear()
            screen.bgcolor("red")
            game_run = False

    #Check for increasing score and reset player position
    if char.ycor() >= 360:
        increase_score()

    #Delete car object when they have moved off screen
    for i in car_class_list:
        if i .xcor() < -400:
            i.hideturtle()
            del i

game_over()
screen.exitonclick()

