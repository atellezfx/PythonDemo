import modulo_saludar # El nombre del módulo se vuelve un namespace

saludo = modulo_saludar.saludar("Alex")
print(saludo)

print(type(modulo_saludar))

# Para ver las propiedades y métodos del namespace
print(dir(modulo_saludar))

# Accediendo al nombre del módulo
print(modulo_saludar.__name__)

# Imprimiendo el nombre del módulo principal main (Que es el que se está ejecutando actualmente)
print(__name__)