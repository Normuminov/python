from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image viewer')

n = 0

def backward():
    global n
    n-=1
    if n < 0: n = len(images) - 1
    img['image'] = images[n]

def forward():
    global n
    n+=1
    if n == len(images): n = 0
    img['image'] = images[n]

images = [
    ImageTk.PhotoImage(Image.open('images/c.png')),
    ImageTk.PhotoImage(Image.open('images/cpp.png')),
    ImageTk.PhotoImage(Image.open('images/c_sharp.png')),
    ImageTk.PhotoImage(Image.open('images/python.png')),
    ImageTk.PhotoImage(Image.open('images/java.png'))
]

img = Label(image=images[n])
img.grid(row=0, column=0, columnspan=3)

Button(root, text='<<', command=backward).grid(row=1, column=0)
Button(root, text='Exit', command=root.quit).grid(row=1, column=1)
Button(root, text='>>', command=forward).grid(row=1, column=2)

root.mainloop()