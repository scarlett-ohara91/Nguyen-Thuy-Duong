n = int(input('your number: ')) #so sanh cai phan ket qua cuoi cung

is_prime = True

for i in range(2,n):
    if n % i == 0:
        print('NOT')
        break
    print('Prime')

