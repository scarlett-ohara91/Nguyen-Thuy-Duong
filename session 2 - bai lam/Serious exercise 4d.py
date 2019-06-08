#Print out n * and xs in total (n is entered by users):
n = int(input('Put the number of stars and s you want: '))
if n % 2 == 0:
    print(int(n/2)* "x * ")
else:
    print(int((n-1)/2)* "x * " + "x")
