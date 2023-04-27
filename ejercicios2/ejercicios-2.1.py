# Faltó el profe y los alumnos van a armar la clase.

# Función para obtener el asistente y al profesor según la edad
def obtener_compañeros(cantidad):
    # Creando la lista con los compañeros
    compañeros = []

    # Ejecutando un ciclo for para pedir información de cada compañero
    for i in range(cantidad):
        nombre = input("Ingresa el nombre: ")
        edad = int(input("Ingresa la edad: "))
        compañero = (nombre, edad)  # Tupla

        # Agregando la información a la lista
        compañeros.append(compañero)

    # Ordenándolos de menor a meyor según la edad
    compañeros.sort(key=lambda x: x[1])  # [0] -> nombre [1] -> edad del compañero

    # compañeros[x] devuelve una tupla con (nombre, edad) y después accedemos al nombre
    # para definir el asistente y al profesor
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]  # -1 es el último elemento de la lista

    # Retornamos una tupla de dos cadenas
    return asistente, profesor


# Desempaquetamos el valor de retorno
asistente, profesor = obtener_compañeros(5)

print(f"El asistente es: {asistente}")
print(f"El profesor es: {profesor}")
