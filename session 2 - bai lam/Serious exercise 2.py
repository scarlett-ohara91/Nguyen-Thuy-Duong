#2.	Write a program that asks users enter a number and then calculates factorial of n: (1 * 2 * 3 *... *n):
n = int(input('Put any number you want: '))
factor = 1
for i in range (2, n + 1):
    factor = factor * i
print(factor)

