from math import sqrt
import random
from turtle import Turtle, Screen


def random_walk(distance):
    turtle.down()
    turtle.width(10)
    r = 0
    g = 0
    b = 0
    r_sign = 1
    g_sign = 1
    b_sign = 1
    for _ in range(distance):
        turtle.forward(random.randint(0, 100))
        turtle.right(random.randint(0, 359))
        r += random.randint(0, 20)*r_sign
        g += random.randint(0, 20)*g_sign
        b += random.randint(0, 20)*b_sign
        if r > 255:
            r_sign = -1
            r = 255
        if g > 255:
            g_sign = -1
            g = 255
        if b > 255:
            b_sign = -1
            b = 255
        if r < 0:
            r_sign = 1
            r = 0
        if g < 0:
            g_sign = 1
            g = 0
        if b < 0:
            b_sign = 1
            b = 0
        colour = (r, g, b)
        turtle.pencolor(colour)
        if abs(turtle.xcor()) > screen1.window_width()/2 or abs(turtle.ycor()) > screen1.window_height()/2:
            turtle.up()
            x = int(random.randint(-screen1.window_width()/2, screen1.window_width()/2))
            y = int(random.randint(-screen1.window_height()/2, screen1.window_height()/2))
            turtle.goto(x, y)
            turtle.down()


dist = 1000
turtle = Turtle()
turtle.speed(10)
screen1 = Screen()
screen1.colormode(255)
random_walk(dist)
screen1.exitonclick()

