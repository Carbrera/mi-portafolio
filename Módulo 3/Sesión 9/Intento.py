def multiplar(a , b = 1):
    return a * b
    
def ingreso_valores_a_calcular():    
    num1 = ingreso_numero('Ingrese el primer número: ')
    num2 = ingreso_numero('Ingrese el segundo número: ')       
    return (num1, num2)

def ingreso_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print('Opción inválida. Debe ingresar un número.')
    
def verificar_opcion():
    num1, num2 = ingreso_valores_a_calcular() 
    return multiplar(num1, num2)
    
def verificar_resultado(resultado):
    if resultado < 0:
        return False         
    
def calculadora():
    while True:
        resultado = verificar_opcion()
        if resultado == None:
            break
        print('El área del rectángulo es: ', resultado)

calculadora()
