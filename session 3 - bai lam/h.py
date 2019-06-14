colors = ['red', 'blue', 'brown', 'yellow', 'grey']
from turtle import *

i = 3

d = int(input('Chieu dai canh mong muon? '))
for clr in colors:
    color(clr) 
    for j in range(i):
        forward(d)
        left(360/i)
    i = i + 1 