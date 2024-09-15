from Evaluacion.plantel import Plantel

class Masajista(Plantel):
    def __init__(self, id, nombre, apellidos, edad, titulacion, annosExperiencia):
        super().__init__(id, nombre, apellidos, edad)
        
        #atributos propios de la clase masajista
        self.titulacion = titulacion
        self.annosExperiencia = annosExperiencia
    
    # Métodos heredados
    def concentrarse(self):
        super().concentrarse()
    
    def viajar(self):
        super().viajar()
    
    # Métodos propios
    def darMasajes(self):
        print("El masajista {} está dando un masaje".format(self.nombre))