'''
Crear una función que sume dos números, otra que reste dos números, otra que multiplique dos números, y otra que divida dos números.
Adicionalmente, crear una función que acepte dos números como parámetros y regrese el resultado en forma de tupla de su suma, resta, multiplicación y división.
Los resultados se deben almacenar en un diccionario, cuyas claves serán: Suma, Resta, Multiplicación y División, y los valores de cada clave serán los resultados obtenidos con la función creada anteriormente. 
'''

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a , b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError('No se puede dividir por cero.')
    else:
        return a / b
    
def resultados(a, b):
    return (sumar(a, b), restar(a, b), multiplicar(a , b), dividir(a, b))

def crear_diccionario(a, b):
    resultado = resultados(a, b)
    diccionario = {
        'sumar': resultado[0],
        'restar': resultado[1],
        'multiplicar': resultado[2],
        'dividir': resultado[3]
    }
    return diccionario

a = float(input('Ingrese un número: '))
b = float(input('Ingrese otro número: '))

resultado = crear_diccionario(a, b)

print(resultado)