choices = {'1.': 35, '2.': 36, '3.': 40, '4.': 44}

print('Answer the following algebra question: \nIf x = 8, then what is the value of 4(x + 3)? \n')
for k, v in choices.items():
    print(k, v)

ans = int(input('Your choice: '))

if ans != 4:
    print(':(')
else:  
    print('Bingo') 