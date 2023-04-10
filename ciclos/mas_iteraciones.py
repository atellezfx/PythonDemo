frutas = ["banana","manzana","ciruela","pera","naranja","granada","durazno"]

# Evitando que se coma una granada
for fruta in frutas:
    if fruta == 'granada':
        continue
    print(f"Me voy a comer una {fruta}")

print("#########################################################################")

# Evitando que se siga comiendo después de una ciruela
for fruta in frutas:
    print(f"Me voy a comer una {fruta}")
    if fruta == 'ciruela':
        break # Cuando se termina en break ya no ejecuta el resto del ciclo incluyendo el else
else:
    print("Terminado el ciclo")

# Recorrer una cadena de texto
cadena = "Benito Bodoque"
for letra in cadena:
    print(letra)

# Ciclo for en una sola línea de código para duplicar cada valor
bitcoins = [2,8,8,10,12]
# Forma estructurada
# numeros_duplicados = list() # Se crea una lista vacía
# for bitcoin in bitcoins:
#     numeros_duplicados.append(bitcoin*2)
# print(numeros_duplicados)
# Forma optimizada
numeros_duplicados = [x*2 for x in bitcoins]
print(numeros_duplicados)