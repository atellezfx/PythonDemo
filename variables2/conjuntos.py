# creando un conjunto a partir de una lista
conjunto1 = set(["dato1", "dato2"])
print(conjunto1)

# Conjuntos anidados
conjunto2 = frozenset(["dato3", "dato4"])
conjunto3 = {conjunto2, "dato5"}
print(conjunto3)

# Teoría de conjuntos
a = {1,3,5,7}
b = {1,3,7}
# Formas de verificar si B es un subconjunto de A
resultado = b.issubset(a)
resultado = b <= a
print(resultado)

# Formas de verificar si A es un superconjunto de B
resultado = a.issuperset(b)
resultado = a >= b
print(resultado)

# Verificando si no existe un valor coincidente
resultado = b.isdisjoint(a)
print(resultado)

