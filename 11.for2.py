# funcion para chequear los numeros pares de una lista.

milista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in milista:
    print(num)


for num in milista: # podemos renombrar el jamon como cualquier nombre con F2. Solo lo seleccionamos y cambia todos los nombres en la funcion
    # chequear por numero pares.
    if num % 2 == 0:
        print(num)
    else:
        print(f'Numero impar: {num}')
