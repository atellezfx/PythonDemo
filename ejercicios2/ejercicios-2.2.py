# Creando una función que nos devuelva los números primos
# entre 0 y el argumento que le pasamos.
def es_primo(num):
    if num < 3: return False
    for i in range(2, num - 1):
        if num % i == 0: return False
    return True


def primos_hasta(num):
    primos = []
    for i in range(num+1):
        if es_primo(i):
            primos.append(i)
    return primos


resultado = primos_hasta(13)
print(resultado)
