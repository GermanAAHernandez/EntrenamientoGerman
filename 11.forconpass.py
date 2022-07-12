# vamos a ver como funciona pass con for

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for item in x:
    # comment
    
# print('fin del libreto de for') # comment me esta generando un error y por lo tanto no imprime nada

for item in x:
    # comment
    pass
    
print('fin del libreto de for') # incluimos pass para omitir el error 'comment' e imprimir el texto 'fin del libreto de for'
