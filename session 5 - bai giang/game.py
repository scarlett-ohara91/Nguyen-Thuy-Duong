from random import randint

notice = ''
x = randint(0,10)
y = randint(0,10)
list_oper = ['+','-','*','/']
oper = list_oper[randint(0,3)]

def eval(x,y,ope):
    if ope == '+':
        return x + y
    if ope == '-':
        return x - y
    if ope == '*':
        return x * y
    if ope == '/':
        return x / y

result = eval(x,y,oper)

# while True:
#     notice = ''
#     x = randint(0,10)
#     y = randint(0,10)
#     list_oper = ['+','-','*','/']
#     oper = list_oper[randint(0,3)]
#     result = 0
#     if oper == '+':
#         result = x + y
#     if oper == '-':   
#         result = x - y
#     if oper == '*':   
#         result = x * y
#     if oper == '/':
#         if y != 0:   
#             result = x / y
#         else:
#             notice = 'Cannot divide a number by 0'
    
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
