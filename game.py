# Click in the righthand window to make it active then use your arrow
# keys to control the spaceship!
import ast
import turtle

screen = turtle.Screen()

# this assures that the size of the screen will always be 400x400 ...
screen.setup(400, 400)

# ... which is the same size as our image
# now set the background to our space image
screen.bgpic("space.jpg")

# Or, set the shape of a turtle
screen.addshape("rocketship.png")
turtle.shape("rocketship.png")

move_speed = 10
turn_speed = 10


# these defs control the movement of our "turtle"
def forward():
    turtle.forward(move_speed)


def backward():
    turtle.backward(move_speed)


def left():
    turtle.left(turn_speed)


def right():
    turtle.right(turn_speed)


turtle.penup()
turtle.speed(0)
turtle.home()

# now associate the defs from above with certain keyboard events
screen.onkey(forward, "Up")
screen.onkey(backward, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.listen()

# -*- coding: utf-8 -*-

# example code snippet py_vuln00: Arbitrary Code Execution:
compute_user_input = input("\nType something here to compute: ")
if not compute_user_input:
    printf("No input")
else:
    print("Result: ", ast.literal_eval(compute_user_input))
