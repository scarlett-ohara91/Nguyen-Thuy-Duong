a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
delta = b**2 - (4*a*c)
if delta < 0:
    print('Vo nghiem')
elif delta == 0:
    print('Nghiem kep')
    print('x = ', (b*-1)/2*a)
else: print('2 nghiem phan biet')