
# spiral_tunnel.py
from turtle import *

size = 50
angle = 20
distance = 50
thickness = 1
speed(0)

for i in range(20):
    # drawing a heptagon
    pendown()
    pensize(thickness)
    circle(size, steps=7)
    penup()

    # increment size and thickness
    size = size + 10
    thickness = thickness + 0.2

    # move start position
    forward(distance)
    left(angle)

hideturtle()
done()
