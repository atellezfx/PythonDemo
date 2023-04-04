## LISTAS
lista = ["Alejandro", "@atellezfx", True, 1.96] # Tipo de dato list
print(lista)
print(lista[0])

## TUPLAS
tupla = ("Alejandro", "@atellezfx", True, 1.96) # Tipo de dato tuple
# Nota: la diferencia de listas y tuplas es que las tuplas son inmutables y no se pueden modificar sus datos
print(tupla[1])

## CONJUNTOS
conjunto = {"Alejandro", "@atellezfx", True, 1.96}
# Nota: Se permite redefinir la referencia pero no los valores y no puede haber duplicados
#       Ademas son colecciones desordenadas.
print(conjunto)
# print(conjunto[1]) No permite acceso directo

## DICCIONARIO (Estilo JSON)
diccionario = {
    'nombre':'Alejandro',
    'emocionado':True,
    'altura': 1.96,
    'canal': '@atellezfx'
}
print(diccionario['canal'])