'''
Diseñe un programa en Python que pida la edad al usuario por consola. 
El usuario debe ingresar un número entero; en caso contrario, el programa arrojará una excepción y le solicitará que ingrese su edad nuevamente. 
Seguidamente, el programa debe imprimir que es Adulto si es mayor o igual a 18; y en caso contrario, no es un adulto. 
'''
class CustomExeption(Exception):
    def __init__(self, mensaje) -> None:
        super().__init__(mensaje)
        
def excepcion_propia():
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            if edad < 0:
                raise CustomExeption('El número ingresado es menor a 0')
            break
        except ValueError as e:
            print("Error, ingrese un numero")
            
        except CustomExeption as e:
            print(e)
            
    if edad >= 18:
        print('El usuario es Adulto')
        
    else:
        print('El usuario no es Adulto')
        
excepcion_propia()