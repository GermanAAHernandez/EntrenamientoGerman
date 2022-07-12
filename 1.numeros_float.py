resultado = 100 / 888
print(resultado)
print('Los resultados son: {}'.format(resultado))

# formateo de float "{valor:width.precision f}"
print('Los resultados son: {r:1.3f}'.format(r = resultado))
print('Los resultados son: {r:10.3f}'.format(r = resultado))
print('Los resultados son: {r:1.5f}'.format(r = resultado))

nombre = 'German'
edad = 44
print('Los resultados son: {}'.format(nombre))

# otra forma de formatear es la siguiente:
print(f'Los resultados son: {nombre}')
print(f'Los resultados son: {nombre} con edad de {edad}')