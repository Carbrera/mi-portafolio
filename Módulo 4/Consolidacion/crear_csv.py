from vehiculos import Automovil, AutoParticular, AutoCarga, Bicicleta, Motocicleta
import csv

def guardar_datos_csv(vehiculos, nombre_archivo):
    try:
        with open(nombre_archivo, "w", newline='') as archivo:
            archivo_csv = csv.writer(archivo)
            for vehiculo in vehiculos:
                archivo_csv.writerow([vehiculo.__class__.__name__, vehiculo.__dict__])
    except Exception as e:
        print(f'Error al guardar los datos: {e}')
    
def leer_datos_csv(nombre_archivo):
    vehiculos = []
    try:
        with open(nombre_archivo, "r") as archivo:
            archivo_csv = csv.reader(archivo)
            for vehiculo in archivo_csv:
                clase, atributos = vehiculo
                vehiculos.append((clase, eval(atributos)))
        return vehiculos
    except Exception as e:
        print(f'Error al leer los datos: {e}')
        return []
    
automovil = Automovil("Ford", "Fiesta", "4", "180", "500")
particular = AutoParticular("Ford", "Fiesta", 4, "180", "500", 5) 
carga = AutoCarga("Daft Trucks", "G 38", 10, 120, "1000", "20000") 
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera") 
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)

vehiculos = [particular, carga, bicicleta, motocicleta]

guardar_datos_csv(vehiculos, 'vehiculos.csv')

automoviles = leer_datos_csv("vehiculos.csv")
for automovil in automoviles:
    clase = automovil[0]
    print(f'\nLista de Vehiculos {clase.lower()}')
    print(automovil)