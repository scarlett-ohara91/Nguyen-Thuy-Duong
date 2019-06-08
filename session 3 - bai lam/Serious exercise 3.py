words = ['champion','name','copy']
from random import *
k = randint(0,len(words)-1)
word_chart = list(words[k])

new = ''

for i in range(len(word_chart)):
    n = randint(0,len(word_chart)-1)
    new = new + word_chart[n]
    del word_chart[n]

print(*new,sep=' ')

print('Let us guess the word: ')
guess = input()
guess2 = list(guess)

c = True

for i in range(len(words[k])): 
    if words[k][i] != guess2[i]: # n = ''.join(word_chart), if guess != n
        print('???')
        c = False
        break

if c == True:
    print('hura')
else:
    print('no')

