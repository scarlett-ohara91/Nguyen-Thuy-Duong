from random import randint

notice = ''
x = randint(0,10)
y = randint(0,10)
list_oper = ['+','-','*','/']
oper = list_oper[randint(0,3)]

from calculator2 import eval            # bo sung cai doan cannot divide by 0

result = eval(x,y,oper)
    
random_result = randint(-1,1)
present_result = random_result + result
if notice != '':
    print(notice)
else:
    print('{0} {1} {2} = {3}'.format(x, oper, y, present_result))                                       #(x, oper, y, '=', present_result)

ans = input('Y/N? ')

if random_result == 0:
    if ans =='Y':
        print('Yay')
    else:
        print('You are wrong')

if random_result != 0:
    if ans =='Y':
        print('You are wrong')
    else:
        print('Yay')
