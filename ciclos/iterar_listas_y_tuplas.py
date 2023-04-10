# La iteración de listas y tuplas es idéntico

animales = ["perro", "gato", "loro", "pez", "hurón"]
numeros = [52,16,14,72]

# Mostrando el contenido de la lista con el ciclo for-in
for animal in animales:
    print(animal)

# Iterando los elementos de la lista y multiplicando sus valores
for num in numeros:
    num *= 10
    print(f"El resultado es: {num}")

# Mostrando el contenido de la lista y su índice en el ciclo for-in
# Primera forma
for tupla in enumerate(animales):
    print(f"{tupla[0]}: {tupla[1]}")
# Segunda forma
for indice, animal in enumerate(animales):
    print(f"{indice}: {animal}")

# Iterando sobre los elementos de dos colecciones de igual longitud al mismo tiempo
personas = ["Alex", "Lucy", "Denver", "Camy", "Kia"]
edades = [44,48,8,8,6]
# Verificamos que ambas colecciones sean del mismo tamaño
assert len(personas) == len(edades)
for persona, edad in zip(personas, edades):
    print(f"{persona} tiene {edad} años")

# Iterando un rango de valores del 5 al 9
for num in range(5,10):
    print(num)

#Iterando un rango de valores del 0 a 4
for num in range(5):
    print(num)

# Usando el else en un ciclo for
for num in numeros:
    print(f"Valor actual: {num}")
else:
    print("El ciclo for ha terminado")