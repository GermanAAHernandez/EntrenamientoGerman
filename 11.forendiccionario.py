# vamos a crear un diccionario con cadena de texto y entero.

dic = {'y1':1, 'y2':5, 'y3':3, 'y4':1, 'y5':2, 'y6':8, 'y7':7, 'y8':8, 'y9':5, 'y10':10}

for item in dic:
    print(item)

# imprimimos cuando queremos ver todo (llave:valor)

for item in dic.items():
    print(item)

# imprimimos solo el valor 

for llaves,valor in dic.items():
    print(valor)

# imprimimos solo la llave

for llaves,valor in dic.items():
    print(llaves)

# imprimimos for values

for value in dic.values():
    print(value)