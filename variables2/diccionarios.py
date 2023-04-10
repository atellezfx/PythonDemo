# Creando diccionarios con dict()
diccionario = dict(nombre="Alex", apellido="Téllez")
print(diccionario)

# Las listas no pueden ser claves pero las tuplas y frozensets si
diccionario = {("Alex", "Lucy"):"Dorset"}
print(diccionario)

# Creando diccionarios con fromkeys()
diccionario = dict.fromkeys(['nombre','apellido'])
print(diccionario)

# Creando un diccionario de un iterable cadena
diccionario = dict.fromkeys("ABCDEFG")
print(diccionario)

