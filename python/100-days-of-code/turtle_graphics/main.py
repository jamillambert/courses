from turtle import Turtle, Screen

turtle = Turtle()
turtle.color("coral")
turtle.shape("turtle")

for i in range(5):
    turtle.forward(150)
    turtle.right(144)
    
my_screen = Screen()
my_screen.exitonclick()
