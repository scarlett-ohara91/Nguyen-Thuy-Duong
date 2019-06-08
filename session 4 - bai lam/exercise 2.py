prices = {"banana": 4,
"apple": 2,
"orange": 1.5,
"pear": 3
}

stock = {"banana": 6,
"apple": 0,
"orange": 32,
"pear": 15
}

#1:
for k, v in prices.items(): # fai 3 lan print ah?
    print(k)
    print('price: ', v)
    print('stock: ', stock[k])

#2:
total = 0
for k, v in prices.items(): 
    n = v * stock[k]
    total = total + n

print(total)
