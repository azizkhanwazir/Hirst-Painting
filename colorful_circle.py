import turtle
import math
import random

# 1) Setup screen
screen = turtle.Screen()
turtle.colormode(255)

# 2) Create the drawing turtle
drawer = turtle.Turtle()
drawer.hideturtle()
drawer.penup()
drawer.speed("fastest")

# 3) Define colors and parameters
colors = [
    (255,   0,   0),   # red
    (255, 165,   0),   # orange
    (255, 255,   0),   # yellow
    (  0, 128,   0),   # green
    (  0, 255, 255),   # cyan
    (  0,   0, 255),   # blue
    (128,   0, 128),   # purple
    (255, 105, 180),   # pink
]
num_dots   = 60       # how many dots around the circle
radius     = 150      # circle radius
dot_size   = 20       # size of each dot

# 4) Draw the circle
for i in range(num_dots):
    angle = math.radians(i * (360 / num_dots))
    x = math.cos(angle) * radius
    y = math.sin(angle) * radius
    drawer.goto(x, y)
    drawer.dot(dot_size, random.choice(colors))

# 5) Wait for click to close
screen.exitonclick()
