# Interpolación
a = 2
b = 10
print(f'La suma de {a} y {b} es {a+b}')

# Dar formato a números flotantes
number = 0.123456789
print(f'Formatear el valor con cuatro dígitos: {number:.4f}')
print(f'Imprimir el valor como un porcentaje: {number:.2%}')
print(f'Imprimir el valor como un porcentaje: {number:.2}')
print(f'Formato exponencial: {number:e}')

# Completar ceros a la izquierda
numbers = [1,10,100]
for num in numbers:
    print(f'El valor con ceros es: {num:04}')

# Indicar que presente el signo en todos los casos
numbers = [-1, 0, 1]
for num in numbers:
    print(f'El valor con signo es: {num:+}')

# Alinear los mensajes a la izquierda (>), a la derecha (<) o al centro (^)
name = 'analytics'
print(f'12345678901234567890')
print(f'{name : >20}')
print(f'{name : <20}')
print(f'{name : ^20}')

# Condiciones para que se incluya una cadena u otra
person = {
    'name': 'Alice',
    'gender': 'female'
}

print(f'{"El usuario" if person.get("gender") == "male" else "La usuaria"} {person.get("name")} se encuentra en línea')

