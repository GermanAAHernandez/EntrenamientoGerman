# los ciclos while van a continuar ejecutando un bloque de codigo while(mientras) una condicion siga siendo verdadera.
# Por ejemplo:, while mi carro no tenga gasolina, sigue hechando gas.
# O while tenga hambre, comer alimentos.

# Sintaxis de un ciclo while
#   while condicion booleana:
#         Ejecutar codigo - hacer algo
# 
# puedes combinar con else:
#   while condicion booleana: 
#         Ejecutar codigo - hacer algo 
#   else:
#         Hacer algo distinto

x = 0

while x < 5:
    print(f'El valor actual de x es: {x}')
    x += 1 # x = x + 1 Es lo mismo que x += 1

# Ejemplo de un ciclo while con else
while x < 5:
    print(f'El valor actual de x es: {x}')
    x += 1 # x = x + 1 Es lo mismo que x += 1
else:
    print('El ciclo termino!')

# Palabras claves que son bien utilizadas en los ciclos while 'break', 'continue' y 'pass'

 