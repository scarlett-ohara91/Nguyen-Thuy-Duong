inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

#1, 2:
inventory['pocket'] = {'seashell', 'strange berry', 'lint'}

#3:
inventory['backpack'].remove('dagger')

#4:
inventory['gold'] = inventory['gold'] + 50

print(inventory)