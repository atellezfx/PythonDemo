def frase(nombre, apellido, adjetivo):
    return f"Hola {nombre} {apellido}, eres muy {adjetivo}"

resultado = frase ("Aljandro", "Téllez", "guapo")
print(resultado)

# Utilizando keyword arguments
resultado = frase(adjetivo="inteligente", apellido="Téllez", nombre="Alejandro")
print(resultado)

# Parámetros opcionales con valores predeterminados
def frase2(nombre, apellido, adjetivo="creativo"):
    return f"Hola {nombre} {apellido}, eres muy {adjetivo}"

resultado = frase2("Alejandro", "Téllez")
print(resultado)