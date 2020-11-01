
# 3.py
from turtle import *

pensize(2)

# circle
fillcolor("pink")
   
begin_fill()
circle(100)
end_fill()

# square
fillcolor("blue")

begin_fill()
circle(100, steps=4)
end_fill()

# triangle
fillcolor("green")

begin_fill()
circle(100, steps=3)
end_fill()

done()

