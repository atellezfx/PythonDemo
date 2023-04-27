def imprime_menu():
    print('Elija una opción')
    menu = {1: 'Suma', 2: 'Resta', 3: 'Multiplicación', 4: 'División', 5: 'Salir'}
    for indice in menu.keys():
        print(f'{indice}: {menu[indice]}')
    return input('Opción: ')


opcion = imprime_menu()
match opcion:
    case '1':
        print('Vamos a sumar dos números')
    case '2':
        print('Vamos a restar dos números')
    case '3':
        print('Vamos a multiplicar dos números')
    case '4':
        print('Vamos a dividir dos números')
    case _:
        print('Saliendo del sistema...')

