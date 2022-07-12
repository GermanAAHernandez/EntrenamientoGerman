mi_lista = [1,2,3,4,5,6,7,8,9,10]
print(mi_lista)

# metodos cadena de texto y numerico con 'len' numero de caracteres
mi_lista = ['german', 1,2,3,4,5,6,7,8,9,10]
print(mi_lista)
print(len(mi_lista))

# metodo indexado
mi_lista = ['uno', 'dos', 'tres']
print(mi_lista[1])

# metodo slicing 
mi_lista = ['uno', 'dos', 'tres']
print(mi_lista[1:])

# metodo sumando con otra lista
mi_lista = ['uno', 'dos', 'tres']
otra_lista = ['cuatro', 'cinco', 'seis']

print(mi_lista + otra_lista)

# metodo de otra manera de sumar las listas
mi_lista = ['uno', 'dos', 'tres']
otra_lista = ['cuatro', 'cinco', 'seis']
nueva_lista = mi_lista + otra_lista

print(nueva_lista)

# metodo de otra manera de sumar las listas y cambia el valor de una de las listas
mi_lista = ['uno', 'dos', 'tres']
otra_lista = ['cuatro', 'cinco', 'seis']
nueva_lista = mi_lista + otra_lista
nueva_lista[0] = 'german'

print(nueva_lista)

# metodo de otra manera de sumar las listas y cambia agregar valores al final de la lista
mi_lista = ['uno', 'dos', 'tres']
otra_lista = ['cuatro', 'cinco', 'seis']
nueva_lista = mi_lista + otra_lista
nueva_lista.append('siete')

print(nueva_lista)

# metodo de otra manera de sumar las listas y removamos valores de una lista
mi_lista = ['uno', 'dos', 'tres']
otra_lista = ['cuatro', 'cinco', 'seis']
nueva_lista = mi_lista + otra_lista
nueva_lista.pop() # remueve el ultimo valor de la lista

print(nueva_lista)

# metodo de otra manera de sumar las listas y removamos valores de una lista
mi_lista = ['uno', 'dos', 'tres']
otra_lista = ['cuatro', 'cinco', 'seis']
nueva_lista = mi_lista + otra_lista
item_popeado = nueva_lista.pop() # saber cual pop es removido de nuestra lista

print(item_popeado)

# metodo de otra manera de sumar las listas y removamos valores de una lista
mi_lista = ['uno', 'dos', 'tres']
otra_lista = ['cuatro', 'cinco', 'seis']
nueva_lista = mi_lista + otra_lista
item_popeado = nueva_lista.pop(3) # saber cual pop es removido de nuestra lista

print(item_popeado)

# metodo de otra manera de sumar las listas y removamos valores de una lista
mi_lista = ['uno', 'dos', 'tres']
otra_lista = ['cuatro', 'cinco', 'seis']
nueva_lista = mi_lista + otra_lista
item_popeado = nueva_lista.pop(-2) # saber cual pop es removido de nuestra lista

print(item_popeado)

# metodo de ordenar las listas
mi_lista = ['a', 'z', 'x', 'b', 'd']
num_lista = [4, 1, 4, 9, 3, 5, 2]

mi_lista.sort()
num_lista.sort()

print(mi_lista, num_lista)

# metodo de ordenar las listas de forma inversa
mi_lista = ['a', 'z', 'x', 'b', 'd']
num_lista = [4, 1, 4, 9, 3, 5, 2]

mi_lista.sort() # ordena la lista
num_lista.sort()

mi_lista.reverse() # ordena la lista de forma inversa
num_lista.reverse()

print(mi_lista, num_lista)