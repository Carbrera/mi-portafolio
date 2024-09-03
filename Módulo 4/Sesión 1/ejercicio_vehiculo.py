#class nombre_objeto:
class Vehiculo:
    # constructor con parametros, se necesitan todos los atributos o parametros para instanciar al objeto
    def __init__(self, marca, color, modelo, peso, ancho, alto):
        self.marca = marca
        self.color = color
        self.modelo = modelo
        self.peso = peso
        self.ancho = ancho
        self.alto = alto
    
    # constructor vacio o construor sin parametros, se pueden omitir los atributos
    def __init__(self, marca=None, color=None, modelo=None, peso=None, ancho=None, alto=None):
        self.marca = marca
        self.color = color
        self.modelo = modelo
        self.peso = peso
        self.ancho = ancho
        self.alto = alto
            
    # funcion para imprimir los objetos en String y no la referencia en memoria del objeto    
    def __str__(self) -> str:
        return f'Vehiculo[ marca:{self.marca}, color:{self.color}, modelo:{self.modelo}, peso:{self.peso}, ancho:{self.ancho}, alto:{self.alto}'    


# instancia de Vehiculo invocando al constructor con parametros        
vehiculo = Vehiculo('BMW', 'Blanco', 'M3', '1500', '2', '1.5')
vehiculo.color = 'Rojo'

vehiculo_cuatro = Vehiculo('VW', 'Blanco', 'Tipo 1', '1346', '1.54', '1.55')

vehiculo_cinco = Vehiculo('Chevrolet', 'Negro', 'Impala', '1831', '2.0', '1.38')

vehiculo_seis = Vehiculo('Toyota', 'Blanco', 'Will', '1140', '1.72', '1.43')

vehiculo_siete = Vehiculo('Aston Martin', 'Negro', 'Lagonda', '2064', '1.83', '4.93')

vehiculo_ocho = Vehiculo('Renault', 'Azul', 'Avantime', '1600', '1.82', '1.62')

# instancia de Vehiculo sin parametros, se omiten los atributos
vehiculo_uno = Vehiculo()
vehiculo_uno.marca = 'Chevrolet' # asignando los atributos del objeto
vehiculo_uno.color = 'Negro'     # asignando los atributos del objeto
vehiculo_uno.modelo = 'Aveo'     # asignando los atributos del objeto
vehiculo_uno.peso = '1500'       # asignando los atributos del objeto
vehiculo_uno.ancho = '2'         # asignando los atributos del objeto

vehiculo_dos = Vehiculo()
vehiculo_dos.marca = 'Susuki' 
vehiculo_dos.color = 'Naranja'
vehiculo_dos.modelo = 'S-Presso'
vehiculo_dos.peso = '1170'
vehiculo_dos.alto = '1.56'
vehiculo_dos.ancho = '1.52'

vehiculo_tres = Vehiculo
vehiculo_tres.marca = 'Fiat'
vehiculo_tres.color = 'Gris'
vehiculo_tres.modelo = 'Multipla'
vehiculo_tres.peso = '1370'
vehiculo_tres.alto = '1.7'
vehiculo_tres.ancho = '1.87'

print(vehiculo)
print(vehiculo_uno)