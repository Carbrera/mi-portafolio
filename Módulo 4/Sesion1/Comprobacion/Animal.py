from multipledispatch import dispatch

class Animal:
    
    @dispatch(str, str, int, float)
    def __init__(self, nombre, raza, edad, peso):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        
    def __init__(self, nombre=None, raza=None, edad=None, peso=None):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        
    def comer(self):
        print('Comiendo')
    
    def caminar(self):
        print('Caminando')
    
    def dormir(self):
        print('Durmiendo')
        
    def __str__(self) -> str:
        return (f' Nombre:{self.nombre}, Raza:{self.raza}, Edad:{self.edad}, Peso:{self.peso}')

perro = Animal()
perro.nombre = 'Brando'
perro.raza = 'San Bernardo' 
perro.edad = '3 años'
perro.peso = '30 kg'

gato = Animal()
gato.nombre = 'Roll'
gato.raza = 'Persa'
gato.edad = '4 años'
gato.peso = '3 kg'


print(f'Perro:{perro}')
print(f'Gato:{gato}')