from turtle import Turtle, Screen

turtle = Turtle()
turtle.color("coral")
turtle.shape("turtle")

for _ in range(4):
    turtle.forward(100)
    turtle.right(90)

screen1 = Screen()
screen1.exitonclick()
