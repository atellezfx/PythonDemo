diccionario = {
    "nombre": "Alejandro",
    "apellido": "Téllez",
    "edad": 44
}
print(diccionario)

# Iterando los elementos de un diccionario
for clave in diccionario:
    print(f"Contenido: {clave}={diccionario.get(clave)}")

# Iterando los elementos de un diccionario, ocupamos items() lo que regresa una tupla de clave/valor
for tupla in diccionario.items():
    print(f"Contenido: {tupla[0]}={tupla[1]}")

