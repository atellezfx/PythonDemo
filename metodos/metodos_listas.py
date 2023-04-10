# Creando una lista con list() aunque no es lo común
# lista = list(["hola", "alex", 44])
lista = ["hola", "alex", 44]
print(lista)

# Obteniendo la cantidad de elementos de la lista
resultado = len(lista);

#Agregando elementos a una lista
lista.append("Camy")

# Insertando un elemento a la lista
lista.insert(3, "Denver")

# Agregando varios elementos a la lista
lista.extend(["Kia", "Tomasito", "Huevito", "Benito"])

# Eliminando un elemento de la lista por su posición
lista.pop(0)

# Eliminando el último elemento de la lista
lista.pop(-1)

# Removiendo un elemento de la lista por su valor, si no lo encuentra arroja excepción
lista.remove(44)

# Eliminando todos los elementos de la lista
#lista.clear()

# Ordenando los elementos de forma ascendente (debe ser una lista homogénea)
# lista.sort()
# lista.sort(reverse=True)

# Invierte los elementos de una lista
lista.reverse()

print(lista)

# Obteniendo el índice de un elemento de la lista (arroja excepción en caso de no encontrarlo)
resultado = lista.index("Camy")

print(resultado)
