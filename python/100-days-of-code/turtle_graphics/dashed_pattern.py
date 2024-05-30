from math import sqrt
from turtle import Turtle, Screen


def dashed_line(length, dash_length):
    dashes = int((length/dash_length)/2)
    for _ in range(dashes):
        turtle.down()
        turtle.forward(dash_length)
        turtle.up()
        turtle.forward(dash_length)
    extra_dist = length - dashes*dash_length*2
    turtle.down()
    turtle.forward(extra_dist)


def dashed_cross():
    turtle.color("coral")
    turtle.shape("turtle")
    turtle.speed(0)
    turtle.up()
    turtle.back(width/2)
    dashed_line(width, width/21)
    turtle.up()
    turtle.back(width/2)
    turtle.left(90)
    turtle.back(height/2)
    dashed_line(height, height/21)


def dashed_diamond():
    turtle.right(135)
    distance = sqrt(height*height/4 + width*width/4)
    turtle.down()
    for _ in range(4):
        dashed_line(distance, distance/21)
        turtle.right(90)


width = 630
height = 630
turtle = Turtle()
turtle.speed(5)
turtle.hideturtle()
dashed_cross()
dashed_diamond()
screen1 = Screen()
screen1.exitonclick()
