from random import *
n = randint(0,101) 
print('your number is:' , n)
if randint(0,101) < 31:
    print('sunny')
elif randint(0,101) < 71:
    print ('rainy')
else:
    print('cloudy')