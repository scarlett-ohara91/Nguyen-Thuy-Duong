x = int(input('x = '))
y = int(input('y = '))
ope = input('ope = ')

# def eval(x,y,ope):
#     if ope == '+':
#         return x + y
#     if ope == '-':
#         return x - y
#     if ope == '*':
#         return x * y
#     if ope == '/':
#         return x / y

# print(eval(9,10,'+'))

result = 0
notice = ''
if ope == '+':
    result = x + y
if ope == '-':
    result = x - y
if ope == '*':
    result = x * y
if ope == '/':
    if y != 0:
        result = x / y
    else:
        notice = 'Cannot divide a number by 0'  # lam sao lap lai voi truong hop nay

if notice == '':
    print(result)
else:
    print(notice)