def saludar(name):
    return f"¡Hola {name}!, Espero que hayas tenido un maravilloso día"

def fibonacci(num):
    a, b = 0, 1
    lista = []
    for i in range(num):
        lista.append(b)
        a, b = b, a + b
    return lista

