"""Print n x m stars ((n, m are entered by users))
Enter n: 5
Enter m: 3
* * * * *
* * * * *
* * * * *"""
n = int(input('Please input the number of stars for each row: '))
m = int(input('Please input the number of rows: '))
for i in range(m):
    print(n * '*') 

