# Creando una función simple
def saludar():
    print("Hola Mundo!!!")


saludar()


# Crear una función con parámetros
def saludar(nombre):
    print(f"Hola {nombre}, bienvenida a Python!")


saludar("Camila")


# Crear una función que nos retorne valores
def generatePassword(num):
    chars = "abcdefghij"
    cadena = str(num)
    num = int(cadena[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num * 2}"
    return contraseña


passwd = generatePassword(45)
frase = f"Tu contraseña nueva es: {passwd}"
print(frase)
