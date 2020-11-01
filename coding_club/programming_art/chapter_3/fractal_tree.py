
# fractal_tree.py
from turtle import *

# set variables
detail = 12 # decrease for more branches
length = 80 # increase for larger tree
thickness = 20 # vary to see effect
angle = 20 # vary to see effect

speed(0)

def draw_tree(branch_thickness, branch_length):
    if branch_length > 5:
        if branch_length < 20:
            color("green")
        else:
            color("brown")

        pensize(branch_thickness)
        forward(branch_length)
        
        right(angle)
        draw_tree(branch_thickness / 1.5, branch_length - detail)
        
        left(2 * angle)
        draw_tree(branch_thickness / 1.5, branch_length - detail)
        
        right(angle)
        back(branch_length)
        color("brown")

# move turtle down the screen and turn to face up
left(90)
penup()
back(100)
pendown()

# set pen color and call the main function
color("brown")
draw_tree(thickness, length)

done()

