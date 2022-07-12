# vamos hacer un ejemplo de continue con for

x = 'German el grande'

for letter in x:
    if letter == 'e':
        continue
    print(letter, end='')

for letter in x:
    if letter == 'a':
        continue
    print(letter, end='')