from Evaluacion.plantel import Plantel

class Futbolista(Plantel):
    def __init__(self, id, nombre, apellidos, edad, dorsal, demarcacion):
        super().__init__(id, nombre, apellidos, edad)
        
        #atributos propios de la clase futbolista
        self.dorsal = dorsal
        self.demarcacion = demarcacion
    
    # Métodos heredados
    def concentrarse(self):
        super().concentrarse()
    
    def viajar(self):
        super().viajar()
    
    # Métodos propios
    def jugarPartido(self):
        print("El futbolista {} está jugando un partido".format(self.nombre))
        
    def entrenar(self):
        print("El futbolista {} está entrenando".format(self.nombre))