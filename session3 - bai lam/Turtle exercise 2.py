colors = ['red', 'blue', 'brown', 'yellow', 'grey']

from turtle import *

for clr in colors:
    color(clr)
    begin_fill()
    for i in range(5):
        forward(100)
        left(90)
    right(90)
    end_fill()
