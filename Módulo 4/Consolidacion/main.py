from vehiculos import Vehiculo, Automovil, AutoParticular, AutoCarga, Bicicleta, Motocicleta

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

main()

particular = AutoParticular("Ford", "Fiesta", 4, "180", "500", 5) 
carga = AutoCarga("Daft Trucks", "G 38", 10, 120, "1000", "20000") 
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera") 
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)

print('\n')
print(particular)
print(carga)
print(bicicleta)
print(motocicleta)
print('\n')
print('Motocicleta es instancia con relación a Vehículo:', isinstance(motocicleta, Vehiculo))
print('Motocicleta es instancia con relación a Automovil:', isinstance(motocicleta, Automovil))
print('Motocicleta es instancia con relación a Vehículo particular:', isinstance(motocicleta, AutoParticular))
print('Motocicleta es instancia con relación a Vehículo de Carga:', isinstance(motocicleta, AutoCarga))
print('Motocicleta es instancia con relación a Bicicleta:', isinstance(motocicleta, Bicicleta))
print('Motocicleta es instancia con relación a Motocicleta:', isinstance(motocicleta, Motocicleta))        