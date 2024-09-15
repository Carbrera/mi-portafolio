class Pato:
    def hablar(self):
        print("¡Cua!, Cua!")

class Perro:
     def hablar(self):
        print("¡Guau, Guau!")
        
class Gato:
    def hablar(self):
        print("¡Miau, Miau!")
        
class Vaca:
    def hablar(self):
        print("¡Muuu, Muuu!")

lista = [Pato(), Perro(), Gato(), Vaca()]

for animal in lista:
    animal.hablar()