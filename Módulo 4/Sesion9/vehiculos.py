class Vehiculo:
    def __init__(self, marca, modelo, nro_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.nro_ruedas = nro_ruedas
        
    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self, marca) -> None:
        self._marca = marca
        
    @property
    def modelo(self):
        return self._modelo
    
    @modelo.setter
    def modelo(self, modelo) -> None:
        self._modelo = modelo
        
    @property
    def nro_ruedas(self):
        return self._nro_ruedas
    
    @nro_ruedas.setter
    def nro_ruedas(self, nro_ruedas) -> None:
        self._nro_ruedas = nro_ruedas
        
    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.nro_ruedas} ruedas"
        
class Automovil(Vehiculo):
    def __init__(self, marca=str, modelo=str, nro_ruedas=int, velocidad=int, cilindraje=int):
        super().__init__(marca, modelo, nro_ruedas)
        self.velocidad = velocidad
        self.cilindraje = cilindraje
        
    @property
    def velocidad(self):
        return self._velocidad
    
    @velocidad.setter
    def velocidad(self, velocidad) -> None:
        self._velocidad = velocidad
        
    @property
    def cilindraje(self):
        return self._cilindraje
    
    @cilindraje.setter
    def cilindraje(self, cilindraje) -> None:
        self._cilindraje = cilindraje
    
    def __str__(self) -> str:
        return super().__str__() + f', {self.velocidad} km/h, {self.cilindraje} cc.'
                
class AutoParticular(Automovil):
    def __init__(self, marca, modelo, ruedas, velocidad, cilindraje, puestos):
        super().__init__(marca, modelo, ruedas, velocidad, cilindraje)
        self.puestos = puestos
        
    def __str__(self) -> str:
        return super().__str__() + f', Puestos: {self.puestos}'

class AutoCarga(Automovil):
    def __init__(self, marca, modelo, ruedas, velocidad, cilindraje, peso_carga):
        super().__init__(marca, modelo, ruedas, velocidad, cilindraje)
        self.peso_carga = peso_carga
        
    def __str__(self) -> str:
        return super().__str__() + f', Carga: {self.peso_carga}'
        
class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, ruedas, tipo):
        super().__init__(marca, modelo, ruedas)
        self.tipo = tipo
        
    def __str__(self) -> str:
        return super().__str__() + f', Tipo: {self.tipo}'
        
class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, ruedas, tipo, motor, cuadro, nro_radios):
        super().__init__(marca, modelo, ruedas, tipo)
        self.motor = motor
        self.cuadro = cuadro
        self.nro_radios = nro_radios
        
    def __str__(self) -> None:
        return super().__str__() + f', Motor: {self.motor}, Cuadro: {self.cuadro}, Nro. Radios: {self.nro_radios}'
    
particular = AutoParticular("Ford", "Fiesta", 4, "180", "500", 5) 
carga = AutoCarga("Daft Trucks", "G 38", 10, 120, "1000", "20000") 
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera") 
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)    