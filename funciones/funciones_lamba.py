# Multiplicando por dos en una función anónima (lambda)
# Las funciones lamba retornan automáticamente
resultado = lambda x: x * 2
print(resultado(5))

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# Creando una función común que diga si es par o no
def es_par(num):
    if num % 2 == 0:
        return True


# Usando filter con una función común
numeros_pares = filter(es_par, numeros)
print(list(numeros_pares))

# Usando filter() con una función lamba
numeros_pares = filter(lambda num: num % 2 == 0, numeros)
print(list(numeros_pares))
