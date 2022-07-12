mi_diccionario = {'llave1': 'valor1', 'llave2': 'valor2', 'llave3': 'valor3'}
print(mi_diccionario)
print(mi_diccionario['llave1'])

# vamos hacer un diccionarios con frutas y valores
mi_diccionario = {'manzanas': '3.24', 'peras': '6.20', 'moras': '8.2102'}
print(mi_diccionario)
print(mi_diccionario['manzanas'])
print(mi_diccionario['peras'])
print(mi_diccionario['moras'])

# vamos hacer un diccionarios con listas dentro frutas y valores
mi_diccionario = {'manzanas': '3.24', 'pai': ['peras', 'fresas'], 'moras': '8.2102'}
print(mi_diccionario)
print(mi_diccionario['manzanas'])
print(mi_diccionario['pai'])
print(mi_diccionario['moras'])

# vamos hacer un diccionarios con listas dentro frutas y llamar peras o fresas
mi_diccionario = {'manzanas': '3.24', 'pai': ['peras', 'fresas'], 'moras': '8.2102'}
print(mi_diccionario)
print(mi_diccionario['manzanas'])
print(mi_diccionario['pai'])
print(mi_diccionario['pai'][1])
print(mi_diccionario['moras'])

# vamos hacer un diccionarios con listas dentro frutas y llamar peras o fresas y con mayuscula todo .upper()
mi_diccionario = {'manzanas': '3.24', 'pai': ['peras', 'fresas'], 'moras': '8.2102'}
print(mi_diccionario)
print(mi_diccionario['manzanas'])
print(mi_diccionario['pai'])
print(mi_diccionario['pai'][1])
print(mi_diccionario['pai'][1].upper())
print(mi_diccionario['moras'])

# vamos hacer un diccionarios y agragar una llave y valor
mi_diccionario = {'manzanas': '3.24', 'pai': ['peras', 'fresas'], 'moras': '8.2102'}

mi_diccionario['gaseosas'] = '2.50'

print(mi_diccionario)

# vamos ver todas las llaves que tenemos en un diccionarios .keys()
mi_diccionario = {'manzanas': '3.24', 'pai': ['peras', 'fresas'], 'moras': '8.2102'}

print(mi_diccionario.keys())

# vamos ver todas los valores que tenemos en un diccionarios .values()
mi_diccionario = {'manzanas': '3.24', 'pai': ['peras', 'fresas'], 'moras': '8.2102'}

print(mi_diccionario.values())

# vamos ver todos los pares que tenemos en un diccionarios .items()
mi_diccionario = {'manzanas': '3.24', 'pai': ['peras', 'fresas'], 'moras': '8.2102'}

mi_diccionario['gaseosas'] = '2.50'

print(mi_diccionario.items())