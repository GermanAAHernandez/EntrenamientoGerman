# Varios objetos en python son 'iterables', significa que podemos iterar sobre cada elemento en el objeto.
# podemos iterar sobre una lista, tupla, diccionario, string, etc.
# podemos iterar atravez de una lista o todos los carccteres en una cadena de texto. string.
# podemos usar ciclos for para ejecutar un bloque de codigo en cada iteracion.

# Sintaxis para un ciclo for

lista_iterable = [1, 2, 3, 4, 5]

for nombre_item in lista_iterable:
    print(nombre_item)

milista = ['Zoila', 'Juan', 'Pedro', 'Maria']

for nombre in milista:
    print(nombre, end=', ')

lista_iterable = [1, 2, 3, 4, 5]

for nombre_item in lista_iterable:
    print('hola')

for nombre_item in lista_iterable:
    print('El numero es: ', nombre_item)

for nombre_item in lista_iterable:
    print('hola', nombre_item + 1)

for nombre_item in lista_iterable:
    print('hola', nombre_item * 2)

