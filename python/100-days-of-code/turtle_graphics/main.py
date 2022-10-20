from math import sqrt
import random
import turtle
import _tkinter

COLOR_STEP = 5
PEN_WIDTH = 1


def random_walk(num_steps, step_length, turtles, width, height):
    """Moves each turtle in the input list {turtles} {num_steps} random steps of up to {step_length} max length"""
    colour = [255, 255, 255]
    colour_sign = [1, 1, 1]
    for _ in range(num_steps):
        (colour, colour_sign) = random_colour_increment(colour, colour_sign)
        for t in turtles:
            t.color(colour)
            t.pencolor(colour)
            t.setheading(random.randint(0, 359))
            t.forward(random.randint(0, step_length))
            if abs(t.xcor()) > width / 2 or abs(t.ycor()) > height / 2:
                random_position(t, width, height)


def spirograph(separation, size, turtles):
    colour = [255, 255, 255]
    colour_sign = [1, 1, 1]
    (colour, colour_sign) = random_colour_increment(colour, colour_sign)
    for _ in range(int(360 / separation)):
        (colour, colour_sign) = random_colour_increment(colour, colour_sign)
        for t in turtles:
            t.color(colour)
            t.pencolor(colour)
            t.circle(size)
            t.setheading(t.heading() + separation)


def dot_grid(num_x, num_y, separation, dot_size, color_list, t):
    """Draws an x by y grid of dots centred on the turtle"""

    corner_x = t.pos()[0] - separation * ((num_x - 1) / 2)  # The number of gaps is num_x-1
    corner_y = t.pos()[1] - separation * ((num_y - 1) / 2)
    t.penup()
    t.hideturtle()
    t.goto(corner_x, corner_y)

    for y in range(num_y):
        for x in range(num_x):
            colour = random.choice(color_list)
            t.dot(dot_size, colour)
            t.forward(separation)
        new_pos_y = t.pos()[1] + separation
        t.goto(corner_x, new_pos_y)
    t.goto(0, 0)


def random_position(t, width, height):
    """Sets the turtle {t} to a random position on the screen"""
    t.up()
    x = int(random.randint(-width / 2, width / 2))
    y = int(random.randint(-height / 2, height / 2))
    t.goto(x, y)
    t.down()


def random_colour_increment(colour, colour_sign):
    """Returns two lists, a list with the colour [r, g, b] and which direction each are moving +/- [1, 1, 1]

    The red green and blue values of the colour are incremented randomly up to the
    amount in the input step value.  If the value goes out of range it is set to the limit
    and the direction in colour_sign is changed so it moves in the opposite direction
    next time"""
    for i in range(3):
        colour[i] += random.randint(0, COLOR_STEP) * colour_sign[i]
        if colour[i] > 255:
            colour_sign[i] = -1
            colour[i] = 255
        if colour[i] < 0:
            colour_sign[i] = 1
            colour[i] = 0
    return colour, colour_sign


def random_colour_list(size, min_rgb, max_rgb):
    """Returns a list of random colours with the input number of elements

    the input is the number of colours and two tuples containing the min and max
    values for red green and blue.  max > min for all colours and all are ints in range (256)"""
    colour_list = []
    for _ in range(size):
        r = random.randint(min_rgb[0], max_rgb[0])
        g = random.randint(min_rgb[1], max_rgb[1])
        b = random.randint(min_rgb[2], max_rgb[2])
        colour = (r, g, b)
        colour_list.append(colour)
    return colour_list


def multiple_turtles(random_start, num_turtles, width, height):
    """Creates a list of turtles and then runs the random_walk on it

    if random_start is true the initial positions are random, if false they all start at (0 ,0)
    Minimise the window to speed up the drawing when large numbers are used"""
    turtle_list = []
    for _ in range(num_turtles):
        t = turtle.Turtle()
        t.speed(0)
        t.down()
        t.hideturtle()
        t.width(PEN_WIDTH)
        if random_start:
            random_position(t, width, height)
        turtle_list.append(t)
    return turtle_list


def main():
    """Creates a screen and then runs the animation, different animations are commented out at the bottom"""

    number_turtles = 100 # Number of turtles for all functions
    number_steps = 1000  # Number of steps in random walk
    max_step_length = 1000  # Maximum step length in random walk
    random_start = True  # If the initial positions are random or at the centre
    separation = 5  # separation of circles in spirograph
    size = 200  # size of circles in spirograph
    min_rgb = (0, 0, 50)  # must be 3 integers between 0 and 255 inclusive
    max_rgb = (200, 200, 200)  # must be 3 integers between 0 and 255 inclusive
    color_list = random_colour_list(100, min_rgb, max_rgb)

    screen = turtle.Screen()
    width = screen.window_width()
    height = screen.window_height()
    screen.colormode(255)
    screen.delay(0)
    screen.tracer(number_turtles, 0)
    turtle_list = multiple_turtles(random_start, number_turtles, width, height)

    # """Spirograph"""
    # try:
    #     spirograph(separation, size, turtle_list)
    #     print("Animation finished")
    #     screen.exitonclick()
    # except (turtle.Terminator, _tkinter.TclError):
    #     print("Window was closed before the animation finished")

    """Random walk"""
    try:
        random_walk(number_steps, max_step_length, turtle_list, width, height)
        print("Animation finished")
        screen.exitonclick()
    except (turtle.Terminator, _tkinter.TclError):
        print("Window was closed before the animation finished")

    # """Dot pattern"""
    # try:
    #     dot_grid(11, 11, 100, 50, color_list, turtle.Turtle())
    #     print("Animation finished")
    #     screen.exitonclick()
    # except (turtle.Terminator, _tkinter.TclError):
    #     print("Window was closed before the animation finished")


main()
