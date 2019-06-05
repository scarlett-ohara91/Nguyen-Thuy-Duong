items = ['T-Shirt', 'Sweater']

times = 0
while True:
    ans = input('Welcome to our shop, what do you want (C, R, U, D)? ').upper()
    times = times + 1
    if ans == 'R':
        print('Our items: ', ','.join(items))
    elif ans == 'C':
        new = input('Enter new item: ')
        items.append(new)
        print('Our items: ', ','.join(items))
    elif ans == 'U':
        upd = int(input('Update position? '))-1
        new = input('New item: ')
        items[upd] = new
        print('Our items: ', ','.join(items))
    elif ans == 'D':
        dele = int(input('Delete position? '))-1
        del items[dele]
        print('Our items: ', ','.join(items))

    if times > 4:
        break
