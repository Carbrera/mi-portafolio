class Animal:
    def __init__(self, nombre, edad, raza, peso):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.peso = peso
        
    def __str__(self) -> str:
        f'Animal(nombre:{self.nombre})'
        
# identificador =  Object(atributos, atributos)       
caballo = Animal('Zeus', 5, 'pura sangre', 450)                   
leon    = Animal('Boulder', 10, 'Atlas', 130)        
