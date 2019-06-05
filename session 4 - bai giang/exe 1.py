cidian = {'ngta':'nguoi ta','ko':'khong','bb':'bye bye'}

while True:
    ques = input('Enter sth: ')
    if ques not in cidian:                  # here?
        contri = input('Want to contribute: ')
        if contri == 'No':
            continue                          # neu ko break?
        if contri == 'Y':
            new = input('Give your meaning: ')
            cidian[ques] = new               # nhu nhau khi co hay ko inden
    
    print(cidian[ques])

# m = 4
# while m < 3:
#     print('hi')
#     m += 2

