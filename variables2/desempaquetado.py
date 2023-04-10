#Creando los datos
datos_en_tupla = ("Alejandro", "Téllez")
datos_en_lista = ["Alejandro", "Téllez"]
datos_en_set = {"Alejandro", "Téllez"}

# El desempaquetado funciona si el número de variables es igual al número de elementos de la colección
nombre,apellido = datos_en_tupla
print(apellido)
print(nombre,apellido)