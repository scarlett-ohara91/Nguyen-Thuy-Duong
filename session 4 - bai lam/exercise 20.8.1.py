sentence = 'ThiS is String with Upper and lower case Letters'
count = {}                  # xem lai cai get()
for character in sentence.lower():
    count[character] = count.get(character,0) + 1   # xem cai cach trong automate

print(count)

list_count = list(count.items())
list_count.sort()
print(list_count)
    