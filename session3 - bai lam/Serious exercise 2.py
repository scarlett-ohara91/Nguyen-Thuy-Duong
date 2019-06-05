sizes = [5, 7, 300, 90, 24, 50, 75]

print('Hello, my name is Hiep and here is my flock' )
print(sizes)
max = 0
for i in sizes:
        if  max < i:
            max = i
print('Now my biggest sheep has size' + ' ' + str(max) + ' ' + 'let us shear it')
index = sizes.index(max)
sizes[index] = 8
print('After shearing, here is my flock')
print(sizes)

n = 1
while True:
    print('MONTH' + ' ' + str(n))
    for i in range(len(sizes)):
        sizes[i] = sizes[i] + 50
    print(str(n) + ' ' + 'month has passed, now here is my flock')
    print(sizes)
    max = 0
    for i in sizes:
        if  max < i:
            max = i
    print('Now my biggest sheep has size' + ' ' + str(max) + ' ' + 'let us shear it')
    index = sizes.index(max)
    sizes[index] = 8
    print('After shearing, here is my flock')
    print(sizes)
    n = n + 1
    if n == 3:
        break
    
print('MONTH 3')
for i in range(len(sizes)):
    sizes[i] = sizes[i] + 50 # nho cai nay
print('3 month has passed, now here is my flock')   
print(sizes)

total = 0
for i in sizes:
    total = total + i
print('My flock has size in total: ' + str(total))
print('I would get' + ' ' +  str(total) + '*2$ = '+ str(total*2)+'$')
