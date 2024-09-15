class Vehiculo:
    def __init__(self, marca, modelo, nro_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.nro_ruedas = nro_ruedas
        
    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.nro_ruedas} ruedas"
        
class Automovil(Vehiculo):
    def __init__(self, marca=str, modelo=str, nro_ruedas=int, velocidad=int, cilindraje=int):
        super().__init__(marca, modelo, nro_ruedas)
        self.velocidad = velocidad
        self.cilindraje = cilindraje
        
    def __str__(self) -> str:
        return super().__str__() + f', {self.velocidad} km/h, {self.cilindraje} cc.'
                
class AutoParticular(Automovil):
    def __init__(self, marca, modelo, ruedas, velocidad, cilindraje, puestos):
        super().__init__(marca, modelo, ruedas, velocidad, cilindraje)
        self.puestos = puestos

class AutoCarga(Automovil):
    def __init__(self, marca, modelo, ruedas, velocidad, cilindraje, peso_carga):
        super().__init__(marca, modelo, ruedas, velocidad, cilindraje)
        self.peso_carga = peso_carga

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, ruedas, tipo):
        super().__init__(marca, modelo, ruedas)
        self.tipo = tipo

class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, ruedas, tipo, nro_radios, cuadro, motor):
        super().__init__(marca, modelo, ruedas, tipo)
        self.nro_radios = nro_radios
        self.cuadro = cuadro
        self.motor = motor