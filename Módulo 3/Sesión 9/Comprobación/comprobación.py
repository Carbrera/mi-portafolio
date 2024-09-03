'''
Crear una función que acepte dos parámetros (base y altura) y calcule el área de un rectángulo. 
Validar que ambos sean números positivos. 
'''

def calcular_area(a, b):
    return a * b

def ingreso_valores():
    num1 = ingreso_numero('Ingrese la base del rectángulo: ')
    num2 = ingreso_numero('Ingrese la altura del rectángulo: ')
    return num1, num2

def ingreso_numero(mensaje):
    while True:
        try:
            num = float(input(mensaje))
            if num > 0:
                return num
            else:
                print('El número debe ser positivo.')
        except ValueError:
            print('Opción inválida. Debe ingresar un número.')

def calculadora_area_rectangulo():
    while True:
        base, altura = ingreso_valores()
        resultado = calcular_area(base, altura)
        print('El área del rectángulo es:', resultado)
        break

calculadora_area_rectangulo()