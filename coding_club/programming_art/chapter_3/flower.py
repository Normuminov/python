
# flower.py
from turtle import *

speed(8)

# set the colour and fill values in one go
color("green", "purple")

# draw the star
begin_fill()

while True:
    forward(150)
    left(170)
    if distance(0, 0) < 1:
        break

end_fill()

hideturtle()
done()

