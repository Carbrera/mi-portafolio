'''
Implementar en Python la clase Persona, que tenga como atributos: nombre, apellidos, sexo, edad, estatura y peso. 
Adicionalmente, se deben implementar los métodos get y set que modifiquen todos los atributos antes mencionados de la clase persona, recordando que los métodos get son los métodos que permiten acceder al estado del objeto persona, y los métodos set permiten modificar el estado de dicho objeto. 
Cree dos objetos de la instancia persona con los siguientes datos: 
Persona_ 1:  Pedro, Vivas, Masculino, 20 años, 1.78 mts, 68 Kg. 
Persona_ 2:  Juan, Camargo, Masculino. 18, 1.8 mts, 75 Kg. 
Modifique en la Persona_1 su edad a 21 años, y a la Persona_2 el apellido a Santiago, y que se muestre por pantalla las actualizaciones respectivas.  
'''


class Persona:
    def __init__(self, nombre, apellido, sexo, edad, altura, peso):
        self.nombre   = nombre
        self.apellido = apellido
        self.sexo     = sexo
        self.edad     = edad
        self.altura   = altura
        self.peso     = peso



    # accesadores y mutadores
    def get_nombre(self):
        return self.nombre
    
    def get_apellido(self):
        return self.apellido
    
    def get_sexo(self):
        return self.sexo
    
    def get_edad(self):
        return self.edad
    
    def get_altura(self):
        return self.altura
    
    def get_peso(self):
        return self.peso
    
    def set_nombre(self, nombre):
        self.nombre = nombre
        
    def set_apellido(self, apellido):
        self.apellido = apellido
        
    def set_sexo(self, sexo):
        self.sexo = sexo
        
    def set_edad(self, edad):
        self.edad = edad
        
    def set_altura(self, altura):
        self.altura = altura
        
    def set_peso(self, peso):
        self.peso = peso
                
    def __str__(self) -> str:
        return f'Persona[ nombre:{self.nombre}, apellido:{self.apellido}, sexo:{self.sexo}, edad:{self.edad}, altura:{self.altura}, peso:{self.peso}'
        
persona_1 = Persona("Pedro", "Vivas", "Masculino", "20 años", "1.78 m", "68 kg")   

persona_2 = Persona("Juan", "Camargo", "Masculino", "18 años", "1.8 m", "75 kg")

print(persona_1)
print(persona_2)
persona_1.set_edad("21 años")
persona_2.set_apellido("Santiago")
print(persona_1)
print(persona_2)