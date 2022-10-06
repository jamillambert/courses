from math import sqrt
import random
from turtle import Turtle, Screen


def random_walk(steps, step_length, turtles):
    colour = [255, 255, 255]
    colour_sign = [1, 1, 1]
    colour_step = 20
    for _ in range(steps):
        (colour, colour_sign) = random_colour(colour, colour_sign, colour_step)
        for turtle in turtles:
            turtle.color(colour)
            turtle.pencolor(colour)
            turtle.right(random.randint(0, 359))
            turtle.forward(random.randint(0, step_length))
            if abs(turtle.xcor()) > screen1.window_width()/2 or abs(turtle.ycor()) > screen1.window_height()/2:
                random_position(turtle)


def random_position(turtle):
    turtle.up()
    x = int(random.randint(-screen1.window_width() / 2, screen1.window_width() / 2))
    y = int(random.randint(-screen1.window_height() / 2, screen1.window_height() / 2))
    turtle.goto(x, y)
    turtle.down()


def random_colour(colour, colour_sign, step):
    for i in range(3):
        colour[i] += random.randint(0, step) * colour_sign[i]
        if colour[i] > 255:
            colour_sign[i] = -1
            colour[i] = 255
        if colour[i] < 0:
            colour_sign[i] = 1
            colour[i] = 0
    return colour, colour_sign


def multiple_turtle_walk():
    steps = 2000
    max_step_length = 20
    number_turtles = 100
    turtle_list = []
    for _ in range(number_turtles):
        turtle = Turtle()
        turtle.color("white")
        turtle.shape("circle")
        turtle.speed(0)
        turtle.down()
        turtle.shapesize(0.5,0.5,1)
        turtle.width(10)
        random_position(turtle)
        turtle_list.append(turtle)
    random_walk(steps, max_step_length, turtle_list)


screen1 = Screen()
screen1.colormode(255)
screen1.delay(0)
multiple_turtle_walk()
screen1.exitonclick()
