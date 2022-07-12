# vamos hacer un ejemplo de break con for

x = 'German el grande'

for letter in x:
    if letter == 'd':
        break
    print(letter, end='')

for letter in x:
    if letter == 'n':
        break
    print(letter, end='')
