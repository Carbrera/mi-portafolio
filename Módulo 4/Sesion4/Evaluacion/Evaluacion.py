class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
            
    def movimiento(self):
        return f'{self.nombre} se está moviendo'

class Maratonista(Persona):
    def movimiento(self):
        return f'{self.nombre} está trotando'

class Ciclista(Persona):
    def movimiento(self):
        return f'{self.nombre} está rodando'
    
persona = Persona('César')
maratonista = Maratonista('Andrea')
ciclista = Ciclista('Carlos')

print(persona.movimiento())
print(maratonista.movimiento())
print(ciclista.movimiento())