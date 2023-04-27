# Creando una función que muestre la serie de fibonacci entre 0 y el número dado

def fibonacci(num):
    a, b = 0, 1
    lista = []
    for i in range(num):
        lista.append(b)
        a, b = b, a + b
    return lista


resultado = fibonacci(10)
print(resultado)
