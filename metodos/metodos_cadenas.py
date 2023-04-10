cadena1 = "Hola soy Alex"
cadena2 = "Bienvenido a Python"

resultado = dir(cadena1)
# Convierte a mayúsculas
resultado = cadena1.upper()
# Convierte a minúsculas
resultado = cadena1.lower()

# Primera letra en mayúscula
resultado = cadena1.capitalize()

# Regresa la posición donde está la primera coincidencia, comenzando por 0
resultado = cadena1.find("soy")

# Buscamos una cadena en otra cadena (si no hay concidencia lanza una excepción)
# resultado = cadena1.index("say")

# Si es numérico, devolvemos True
resultado = cadena1.isnumeric()

# Si es alfanumérico, devolvemos True, el espacio no es alfanumérico
resultado = cadena1.isalpha()

# Si es contiene números y letras, devolvemos True
resultado = cadena1.isalnum()

# Contar coincidencias
resultado = cadena1.lower().count("a")

# Contar la cantidad de caracteres
resultado = len(cadena1)

# Verificamos si una cadena empieza con un determinado texto, y regresa True en caso de encontrarla
resultado = cadena1.startswith("Ho")

# Verificamos si una cadena termina con un determinado texto, y regresa True en caso de encontrarla
resultado = cadena1.endswith("lex")

# Reemplaza un valor por otro
resultado = cadena1.replace("Hola", "Que jáis?")

# Separa la cadena por el parámetro dato, regresando una lista
resultado = cadena1.split(" ")

print( resultado )
