numeros = [4,7,1,42,15]
# Encontrando el valor más grande de una lista, tupla o conjunto (Si no son números arroja una excepción)
print( max(numeros) )

# Encontrando el valor más bajo de una lista, tupla o conjunto (Si no son números arroja una excepción)
print( min(numeros) )

# Redondeando a 2 decimales (Si no son números arroja una excepción)
print( round( 12.345678, 2 ) )

# Retorna False para valores 0 o vacío y True para valores diferente de 0 o que no estén vacíos
print(bool(0))
print(bool(None))
print(bool(list()))
print(bool(1))

# Retorna True si todos los valores on verdaderos (Si no son números arroja una excepción)
print( all(numeros) ) # Verdadero
print( all([0,1,2,3,4]) ) # Falso

# Suma todos los valores de un iterable (Si no son números arroja una excepción)
print(sum(numeros))