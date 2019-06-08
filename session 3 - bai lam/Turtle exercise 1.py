colors = ['red', 'blue', 'brown', 'yellow', 'grey']
from turtle import *

i = 3
# tong so goc = 180*(n-2), vay so do cua moi goc  = 180 - (360/n)
d = int(input('Chieu dai canh mong muon? '))
for clr in colors:
    color(clr) # nho cai doan nay
    for j in range(i):
        forward(d)
        left(360/i)
    i = i + 1 # xem lai doan nay