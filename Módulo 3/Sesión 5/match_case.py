#match case

opcion = input('Hola. Bienvenido\n'
               + 'Selecciona una opción\n'
               + '1.- Opción 1\n'
               + '2.- Opción 2\n'
               + '3.- Opción 3\n'
               + '4.- Salir'
)


match opcion:
    case '1':
        print('Opción 1')
    case '2':
        print('Opción 2')
    case '3':
        print('Opción 3')
    case '4':
        print('Hasta luego')
    case _:
        print('Opción no válida')