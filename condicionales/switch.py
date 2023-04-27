# A partir de la versión 3.10 se implementó el equivalente al switch

color = input("Ingrese un color: ")

match color.lower():
    case 'verde':
        print('EL color es verde')
    case 'rojo':
        print('El color es rojo')
    case 'azul':
        print('El color es azul')
    case _: # Equivale al default
        print('No es el color correcto')