# Aplicando alias a los métodos importados de modulo_saludar
from modulo_saludar import saludar, fibonacci as fibo

# Importando todo el contenido del módulo modulo_saludar
# aunque es una mala práctica importar todo el contenido
# from modulo_saludar import *

saludo = saludar("Alex")
print(saludo)

resultado = fibo(10)
print(resultado)
