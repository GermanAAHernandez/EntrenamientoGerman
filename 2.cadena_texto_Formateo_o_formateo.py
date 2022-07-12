
print('esto es una cadena de {}'.format('texto'))
print('esto {} {} {}'.format('es', 'una', 'cadena'))
print('esto {0} {1} {2}'.format('es', 'una', 'cadena'))
print('esto {e} {u} {c}'.format(e = 'es', u = 'una', c = 'cadena'))
print('esto {0} {0} {0}'.format('es', 'una', 'cadena'))
print('esto {2} {0} {1}'.format('es', 'una', 'cadena'))
print('esto {0} {1} {2} {3}'.format('es', 'una', 'cadena', 'de texto'))
print('esto {e} {u} {c} {d}'.format(e = 'es', u = 'una', c = 'cadena', d = 'de texto'))

resultados = 100/888
print("El resultado es {}".format(resultados))
print("El resultado es {:.2f}".format(resultados)) # {:.2f} es para decimales. formateo de float '{valor:width.precision f}'
print("El resultado es {:.3f}".format(resultados)) # {:.3f} es para decimales. formateo de float '{valor:width.precision f}'
print("El resultado es {:.4f}".format(resultados)) # {:.4f} es para decimales. formateo de float '{valor:width.precision f}'

print("El resultado es {r:.2f}".format(r = resultados)) # {:.2f} es para decimales. formateo de float '{valor:width.precision f}'
print("El resultado es {r:.3f}".format(r = resultados)) # {:.3f} es para decimales. formateo de float '{valor:width.precision f}'
print("El resultado es {r:.4f}".format(r = resultados)) # {:.4f} es para decimales. formateo de float '{valor:width.precision f}'

print("El resultado es {r:20.4f}".format(r = resultados)) # {:20.4f} es para decimales. 20 es la cantidad de espacios anticipados antes de imprimir

nombre = 'German'
edad = '44 años'
print(f'Mi nombre es {nombre} con edad de {edad}')