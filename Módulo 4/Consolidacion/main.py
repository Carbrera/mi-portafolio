from vehiculos import Automovil

#auto1 = Automovil('Toyota', 'Yaris', 4, 120, 800)
#auto2 = Automovil('Fiat', 'Palio', 4, 95, 1200)
#auto3 = Automovil('Ford', 'Fiesta', 4, 125, 1500)

def main():
    autos = []
    cantidad = int(input('Cuántos vehículos desea insertar: '))

    for i in range(cantidad):
        print(f'\nDatos del automóvil {i + 1}')
        marca = input('Inserte la marca del automóvil: ')
        modelo = input('Inserte el modelo del automóvil: ')
        nro_ruedas = int(input('Inserte el número de ruedas: '))
        velocidad = int(input('Inserte la velocidad en km/h: '))
        cilindraje = int(input('Inserte el cilindraje en cc: '))

        automovil = Automovil(marca, modelo, nro_ruedas, velocidad, cilindraje)
        autos.append(automovil)

    print('\nImprimiendo por pantalla los Vehículos:')
    for i, autos in enumerate(autos, 1):
        print(f'Datos del automóvil {i} : {autos}')


if __name__ == '__main__':
    main()