from tkinter import *

root = Tk()
root.title('Calculator')

def click(value):
    if display.get() == '0' and value != '.':
        display.delete(0, END)
        answer['text'] = '= 0'

    temp = display.get()
    display.delete(0, END)

    if value == '\b':    
        display.insert(0, temp[:-1])
    elif value == '\r':
        display.insert(0, 0)
    elif value in '+-*/%=' and temp[-1] in '+-*/=':
        display.insert(0, temp[:-1] + value)
    else:
        display.insert(0, temp + value)
    
    try: answer['text'] = '= ' + str(eval(display.get()))
    except: pass

# Define and put on the screen the display

display = Entry(root, width=30, borderwidth=5)
display.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
display.insert(0, 0)

# Creating answer label

answer = Label(root, text='= 0')
answer.grid(row=0, column=3)

# Define buttons

button_0 = Button(root, text='0', padx=87, pady=20, command=lambda: click('0'))
button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: click('1'))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: click('2'))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: click('3'))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: click('4'))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: click('5'))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: click('6'))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: click('7'))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: click('8'))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: click('9'))

button_dot = Button(root, text='.', padx=42, pady=20, command=lambda: click('.'))
button_add = Button(root, text='+', padx=39, pady=20, command=lambda: click('+'))
button_sub = Button(root, text='-', padx=42, pady=20, command=lambda: click('-'))
button_mul = Button(root, text='*', padx=41, pady=20, command=lambda: click('*'))
button_div = Button(root, text='/', padx=42, pady=20, command=lambda: click('/'))
button_equal = Button(root, text='=', padx=39, pady=20, command=lambda: click('='))
button_clear = Button(root, text='AC', padx=35, pady=20, command=lambda: click('\r'))
button_del = Button(root, text='Del', padx=33, pady=20, command=lambda: click('\b'))
button_mod = Button(root, text='%', padx=37, pady=20, command=lambda: click('%'))

# Put the buttons on the screen

button_0.grid(row=5, column=0, columnspan=2)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_dot.grid(row=5, column=2)
button_add.grid(row=1, column=3)
button_sub.grid(row=2, column=3)
button_mul.grid(row=3, column=3)
button_div.grid(row=4, column=3)
button_equal.grid(row=5, column=3)
button_clear.grid(row=1, column=0)
button_del.grid(row=1, column=1)
button_mod.grid(row=1, column=2)

root.mainloop()
