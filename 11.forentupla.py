# crear una lista en la que cuente con tuplas.

milista = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
print(len(milista))

for item in milista:
    print(item)

# imprimir las variables que estan dentro de una tupla

for (a, b) in milista:
    print(a)
    print(b)