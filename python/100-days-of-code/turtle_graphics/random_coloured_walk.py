from math import sqrt
import random
import turtle
import _tkinter


def random_walk(num_steps, step_length, turtles):
    """Moves each turtle in the input list {turtles} {num_steps} random steps of up to {step_length} max length"""
    colour = [255, 255, 255]
    colour_sign = [1, 1, 1]
    colour_step = 10
    for _ in range(num_steps):
        (colour, colour_sign) = random_colour(colour, colour_sign, colour_step)
        for t in turtles:
            t.color(colour)
            t.pencolor(colour)
            t.setheading(random.randint(0, 359))
            t.forward(random.randint(0, step_length))
            if abs(t.xcor()) > screen1.window_width() / 2 or abs(t.ycor()) > screen1.window_height() / 2:
                random_position(t)


def random_position(t):
    """Sets the turtle {t} to a random position on the screen"""
    t.up()
    x = int(random.randint(-screen1.window_width() / 2, screen1.window_width() / 2))
    y = int(random.randint(-screen1.window_height() / 2, screen1.window_height() / 2))
    t.goto(x, y)
    t.down()


def random_colour(colour, colour_sign, step):
    """Returns two lists, a list with the colour [r, g, b] and which direction each are moving +/- [1, 1, 1]

    The red green and blue values of the colour are incremented randomly up to the
    amount in the input step value.  If the value goes out of range it is set to the limit
    and the direction in colour_sign is changed so it moves in the opposite direction
    next time"""
    for i in range(3):
        colour[i] += random.randint(0, step) * colour_sign[i]
        if colour[i] > 255:
            colour_sign[i] = -1
            colour[i] = 255
        if colour[i] < 0:
            colour_sign[i] = 1
            colour[i] = 0
    return colour, colour_sign


def multiple_turtle_walk(random_start, num_turtles, max_step, num_steps):
    """Creates a list of turtles and then runs the random_walk on it

    if random_start is true the initial positions are random, if false they all start at (0 ,0)
    Minimise the window to speed up the drawing when large numbers are used"""
    turtle_list = []
    screen1.tracer(num_turtles, 0)
    for _ in range(num_turtles):
        t = turtle.Turtle()
        t.speed(0)
        t.down()
        t.hideturtle()
        t.width(1)
        if random_start:
            random_position(t)
        turtle_list.append(t)
    try:
        random_walk(num_steps, max_step, turtle_list)
        return True
    except (turtle.Terminator, _tkinter.TclError):
        print("Window was closed before the animation finished")
        return False


# Creates a screen and then runs the animation
# Minimise the window to speed up the drawing
screen1 = turtle.Screen()
screen1.colormode(255)
screen1.delay(0)
number_turtles = 1
number_steps = 10000
max_step_length = 10
if multiple_turtle_walk(True, number_turtles, max_step_length, number_steps):
    print("Animation finished")
    screen1.exitonclick()
