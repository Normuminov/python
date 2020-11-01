
# many_circles.py
from turtle import *

# set variables
size = 50
distance = 50
angle = 20

# speed things up
speed(0)

# draw the pattern
for i in range(18):
    # draw a circle
    pendown()
    circle(size)
    penup()

    # move start position
    forward(distance)
    left(angle)

# hide the turtle when it has finished drawing
hideturtle()

done()

