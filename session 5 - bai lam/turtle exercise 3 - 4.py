from turtle import *

def draw_square(lg,clr):
    color(clr)
    for i in range(4):
        forward(lg)     # dat 1 i nua o day dc ko?
        left(90)
 

for i in range(30):
   draw_square(i * 5, 'red')
   left(17)
   penup()
   forward(i * 2)
   pendown()