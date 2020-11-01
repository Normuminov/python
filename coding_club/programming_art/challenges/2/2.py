
# 2.py
from turtle import *

pensize(3)
fillcolor("red")

circle(100, steps=4)    # square

# move to the centre of the square
penup()
left(90)
forward(50)
pendown()
right(90)

begin_fill()
circle(50)              # circle
end_fill()

done()

