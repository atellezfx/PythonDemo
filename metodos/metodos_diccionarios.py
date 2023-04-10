diccionario = {
    "nombre": "Alejandro",
    "apellido": "Téllez",
    "edad": 44
}

# Obteniendo un elemento del diccionario, en caso de no encontrarlo regresa None
nombre = diccionario.get("nombre")

# Obteniendo un elemento del diccionario, en caso de no encontrarlo arroja una excepción
# nombre = diccionario["nombres"]
print(nombre)

# Obteniendo una objeto dict de las llaves, el cual es iterable
claves = diccionario.keys()
print(claves)

# Eliminando todos los elementos del diccionario
# diccionario.clear()

# ELiminando un elemento del diccionario (Arroja excepción en caso de no encontrarlo)
diccionario.pop("edad")

# Obteniendo un objeto dict iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)