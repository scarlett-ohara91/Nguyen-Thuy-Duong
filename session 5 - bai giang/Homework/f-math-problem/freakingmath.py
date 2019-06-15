from random import *

def eval(x,y,oper):
    if oper == '+':
        return x + y
    if oper == '-':
        return x - y
    if oper == '*':
        return x * y
    if oper == '/':
        return x / y


def generate_quiz():
    from random import randint

    x = randint(1,10)
    y = randint(1,10)
    list_oper = ['+','-','*','/']
    oper = list_oper[randint(0,3)]

    result_raw = eval(x,y,oper)
    random_result = randint(-1,1)
    result = random_result + result_raw

    return [x, y, oper, result]

def check_answer(x, y, op, result, user_choice):
    if eval(x,y,op) == result:
        if user_choice == True:
            return True
        else:
            return False
    elif eval(x,y,op) != result:
        if user_choice == True:
            return False
        else:
            return True
