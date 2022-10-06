from math import sqrt
import random
from turtle import Turtle, Screen


def random_walk(distance):
    turtle.down()
    turtle.width(10)
    for _ in range(distance):
        turtle.forward(random.randint(0, 100))
        turtle.right(random.randint(0, 359))
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colour = (r, g, b)
        turtle.pencolor(colour)
        if abs(turtle.xcor()) > screen1.window_width()/2 or abs(turtle.ycor()) > screen1.window_height()/2:
            turtle.goto(0, 0)


dist= 1000
turtle = Turtle()
turtle.speed(10)
screen1 = Screen()
screen1.colormode(255)
random_walk(distance)
screen1.exitonclick()

