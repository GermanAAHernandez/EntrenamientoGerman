# Declaraciones if, else, elif
# python usa un sistema de identacion al momento que declaramos funciones y logica con if, else, elif
# Se llama 'control flow syntax' y usamos : e identacion (espacios en blanco)
# Este sistema de identacion es muy importante y es lo que separa a python del resto de lenguajes.

# Sintaxis de una declaracion if

# if alguna_condicion:
    # Ejecutamos codigo

# sintaxis de una declaracion if con else

# if alguna_condicion:
    # Ejecutamos codigo 
# else:
    # Aplicar algo mas.

# sintaxis de una declaracion elif

# if alguna_condicion:
    # Ejecutamos codigo
# elif otra_condicion:
    # algo distinto     
# else:
    # Aplicar algo mas.

if True:
    print(True)

hambre = True

if hambre:
    print('tenenos hambre!')

hambre = False

if hambre:
    print('tenenos hambre!')
else:
    print('Estamos llenos!')

hambre = True
sed = True

if hambre and not sed:
    print('tenenos hambre!')
elif hambre == True and sed == True:
    print('tenenos hambre y sed!')
else:
    print('Estamos llenos!')


