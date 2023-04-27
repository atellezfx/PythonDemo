
import sys
from os import getcwd, chdir

# ruta_actual = "/home/alejandro/PycharmProjects/PythonDemo"
ruta_actual = sys.path[0]
sys.path.append( f"{ruta_actual}/../modulos/" )

print( sys.path )

print( getcwd() )
chdir("..")
print( getcwd() )

import modulo_saludar as ms

fibo = ms.fibonacci(5)
print(fibo)