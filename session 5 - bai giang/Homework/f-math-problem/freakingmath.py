from random import *

def eval(x,y,ope):
    if ope == '+':
        return x + y
    if ope == '-':
        return x - y
    if ope == '*':
        return x * y
    if ope == '/':
        return x / y


def generate_quiz():
    from random import randint

    x = randint(0,10)
    y = randint(0,10)
    list_oper = ['+','-','*','/']
    oper = list_oper[randint(0,3)]

    result = eval(x,y,oper)
    random_result = randint(-1,1)
    present_result = random_result + result

    return [x, y, oper, present_result]

def check_answer(x, y, op, result, user_choice):
    pass
