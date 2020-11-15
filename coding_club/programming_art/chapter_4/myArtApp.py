# myArtApp.py
# based on the code from myEtchASketch.py in Python Basics

from tkinter import *

#### Set variables:
canvas_height = 400
canvas_width = 600
canvas_colour = "black"
x_coord = canvas_width/2
y_coord = canvas_height
line_colour = "red"
line_width = 5
line_length = 5

## new variables go here:
background = "image/treescape.gif"
pen_up = False
current_line = None

#### Functions:
def move(x, y):
    global x_coord
    global y_coord
    new_x_coord = x_coord + x
    new_y_coord = y_coord + y
    ## add the pen_up code here:
    if (pen_up == False):
        canvas.create_line(x_coord, y_coord, new_x_coord, new_y_coord, width=line_width, fill=line_colour)
    
    canvas.create_line(x_coord, y_coord, new_x_coord, new_y_coord,
                       width=line_width, fill=line_colour)
    x_coord = new_x_coord
    y_coord = new_y_coord
    
def move_N(event):
    move(0, -line_length)

def move_S(event):
    move(0, line_length)

def move_E(event):
    move(line_length, 0)
    
def move_W(event):
    move(-line_length, 0)
    
def erase_all(event):
    canvas.delete(ALL)

## add new functions here:
def pen_lift(event):
    global pen_up
    pen_up = True

def pen_down(event):
    global pen_up
    pen_up = False

#### main:
window = Tk()
window.title("MyArtApp")
canvas = Canvas(bg=canvas_colour, height=canvas_height,
                width=canvas_width, highlightthickness=0)

## background image code goes here:
scene = PhotoImage(file=background)
canvas.create_image(0, 0, image=scene, anchor=NW)

canvas.pack()

# bind movement to keys
window.bind("<Up>", move_N)
window.bind("<Down>", move_S)
window.bind("<Left>", move_W)
window.bind("<Right>", move_E)
window.bind("e", erase_all)
window.bind("u", pen_lift)
window.bind("d", pen_down)

# start tkinter's main loop
window.mainloop()
