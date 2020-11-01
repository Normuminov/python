
# colourful.py
from turtle import *

# set variables
size = 50
distance = 50
angle = 20
speed(0)
shape("turtle")
bgcolor("blue")
pensize(4)

for i in range(18):
    # draw a square
    pendown()
    color("yellow")
    circle(size, steps=4)
    penup()

    # move start position
    forward(distance)
    left(angle)

setposition(5, 30)
distance = 40

for i in range(18):
    # draw a circle
    pendown()
    color("orange")
    circle(size)
    penup()

    # move start position
    forward(distance)
    left(angle)

# move turtle
setposition(22, 144)
color("red")

done()

