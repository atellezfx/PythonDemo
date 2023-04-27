# Si el módulo estuviera dentro de una carpeta en la misma ruta
from funciones.utilerias import fibonacci, saludar

saludo = saludar("Alex")
print(saludo)

lista = fibonacci(20)
print(lista)

# Imprimiendo el nombre del módulo principal main (Que es el que se está ejecutando actualmente)
print(__name__)