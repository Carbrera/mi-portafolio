from Evaluacion.plantel import Plantel

class Entrenador(Plantel):
    def __init__(self, id, nombre, apellidos, edad, idFederacion):
        super().__init__(id, nombre, apellidos, edad)
        
        #atributos propios de la clase entrenador
        self.idFederacion = idFederacion
    
    # Métodos heredados
    def concentrarse(self):
        super().concentrarse()
    
    def viajar(self):
        super().viajar()
    
    # Métodos propios
    def dirigirPartido(self):
        print("El entrenador {} está dirigiendo un partido".format(self.nombre))
        
    def dirigirEntrenamiento(self):
        print("El entrenador {} está dirigiendo un entrenamiento".format(self.nombre))