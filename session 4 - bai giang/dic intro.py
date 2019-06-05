person = {'name':'Duc','age':22,'ex-gf':3,'uni':'FTU'}
name = person['name']
print(name)

# for k,v in person.items():
#     print(k + ':' + str(v))

# person['major'] = 'chinese'

# person['age'] = 25
# print(person)

del person['age']
print(person)