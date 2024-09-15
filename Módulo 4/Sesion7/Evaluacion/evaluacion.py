'''
Diseñe una nueva clase de excepción definida por el usuario, que gestione la entrada del valor de una variable salario, y la misma se encuentre entre los valores de 1000 y 2000; de lo contrario, se lanza una excepción que refleja que el salario no se encuentra en el rango de 1000 y 2000. 
'''

class RangoSalarioError(Exception):
    def __init__(self, mensaje, salario) -> None:
        super().__init__(mensaje)
        self.salario = salario
        self.mensaje = mensaje
        
    def __str__(self) -> str:
        return f'{self.salario} -> {self.mensaje}'

def validar_salario():
    try:
        salario = int(input('Ingrese un salario: '))
        if not (1000 <= salario <= 2000):
            raise RangoSalarioError('Salario no está definido en el rango (1000 a 2000)', salario)
        print(f'El salario {salario} se encuentra denro del rango')
    except Exception as e:
        print('Error: ', str(e))
    
validar_salario()