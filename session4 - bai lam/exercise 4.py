choices = {'1.': 35, '2.': 36, '3.': 40, '4.': 44}

print('1. Answer the following algebra question: \nIf x = 8, then what is the value of 4(x + 3)? \n')
for k, v in choices.items():
    print(k, v)

ans = int(input('Your choice: '))

count1 = 0
if ans != 4:
    print(':(')
else:  
    print('Bingo') 
    count1 = count1 + 1

choices = {'1.': 'About 55', '2.': 'About 65', '3.': 'About 75', '4.': 'About 85'}

print('2. Estimate this answer(exact calculation not needed) \nJack scoed these marks in 5 math tests : 49, 81, 72, 66 and 52. What is the mean?')
for k, v in choices.items():
    print(k, v)

ans = int(input('Your choice: '))


count2 = 0
if ans != 2:
    print(':(')
else:  
    print('Bingo') 
    count2 = count2 + 1

print('You correctly answered', count1 + count2, 'out of 2 questions')