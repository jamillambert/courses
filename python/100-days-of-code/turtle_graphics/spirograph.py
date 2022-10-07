from math import sqrt
import random
import turtle
import _tkinter
COLOR_STEP = 40
PEN_WIDTH = 1


def random_walk(num_steps, step_length, turtles, width, height):
    """Moves each turtle in the input list {turtles} {num_steps} random steps of up to {step_length} max length"""
    colour = [255, 255, 255]
    colour_sign = [1, 1, 1]
    for _ in range(num_steps):
        (colour, colour_sign) = random_colour(colour, colour_sign)
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
    (colour, colour_sign) = random_colour(colour, colour_sign)
    for _ in range(int(360 / separation)):
        (colour, colour_sign) = random_colour(colour, colour_sign)
        for t in turtles:
            t.color(colour)
            t.pencolor(colour)
            t.circle(size)
            t.setheading(t.heading() + separation)


def random_position(t, width, height):
    """Sets the turtle {t} to a random position on the screen"""
    t.up()
    x = int(random.randint(-width / 2, width / 2))
    y = int(random.randint(-height / 2, height / 2))
    t.goto(x, y)
    t.down()


def random_colour(colour, colour_sign):
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
    # Creates a screen and then runs the animation

    number_turtles = 1
    number_steps = 10000
    max_step_length = 10
    random_start = False
    separation = 5
    size = 200

    screen = turtle.Screen()
    width = screen.window_width()-500
    height = screen.window_height()-500
    screen.colormode(255)
    screen.delay(0)
    screen.tracer(number_turtles, 0)
    turtle_list = multiple_turtles(random_start, number_turtles, width, height)
    try:
        spirograph(separation, size, turtle_list)
        print("Animation finished")
        screen.exitonclick()
    except (turtle.Terminator, _tkinter.TclError):
        print("Window was closed before the animation finished")

    # try:
    #     random_walk(number_steps, max_step_length, turtle_list, width, height)
    #     print("Animation finished")
    #     screen.exitonclick()
    # except (turtle.Terminator, _tkinter.TclError):
    #     print("Window was closed before the animation finished")

main()