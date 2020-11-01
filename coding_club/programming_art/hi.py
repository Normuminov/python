
from turtle import *

# change line width
pensize(5)

# change to an actual turtle
shape("turtle")

# draw the letter H
left(90)
forward(100)
back(50)
right(90)
forward(40)
left(90)
forward(50)
back(100)

# move to start of next letter
penup()
right(90)
forward(40)
left(90)
pendown()

# draw the letter i
forward(50)
penup()
forward(25)

# tell Python t ostop waiting for turtle instructions
done()

