# Forma no optima de sumar valores
def suma(lista):
    total = 0
    for num in lista:
        total += num
    return total


resultado = suma([5,3,9,10,20,3])
print(resultado)

# Utilizando el operador * como agumento (*args)
def suma_args(*numeros):
    return sum(numeros)

resultado = suma_args(5,3,9,10,20,3)
print(resultado)

def suma_args2(nombre, *numeros):
    return f"{nombre}, la suma de tus números es {sum(numeros)}"

resultado = suma_args2("Alex", 5,3,9,10,20,3)
print(resultado)