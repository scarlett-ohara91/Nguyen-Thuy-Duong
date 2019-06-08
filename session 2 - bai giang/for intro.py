from turtle import *
shape ("turtle")
speed(-1)
n = 30
for i in range(10):
    for j in range(2):
        forward(n)
        left(90)
    n = n +20
mainloop()