# La iteración de conjuntos

animales = {"perro", "gato", "loro", "pez", "hurón"}
numeros = {52,16,14,72}

# Mostrando el contenido del conjunto con el ciclo for-in
for animal in animales:
    print(animal)

# Iterando los elementos del conjunto y multiplicando sus valores
for num in numeros:
    num *= 10
    print(f"El resultado es: {num}")

# Mostrando el contenido del conjunto y su índice en el ciclo for-in
# Primera forma
for tupla in enumerate(animales):
    print(f"{tupla[0]}: {tupla[1]}")
# Segunda forma
for indice, animal in enumerate(animales):
    print(f"{indice}: {animal}")

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