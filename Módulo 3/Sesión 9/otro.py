# Funciones básicas para operaciones aritméticas
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

# Función que retorna una tupla con los resultados de las operaciones
def calcular_todas(a, b):
    return (sumar(a, b), restar(a, b), multiplicar(a, b), dividir(a, b))

# Función que almacena los resultados en un diccionario
def almacenar_resultados(a, b):
    resultados = calcular_todas(a, b)
    diccionario_resultados = {
        "Suma": resultados[0],
        "Resta": resultados[1],
        "Multiplicación": resultados[2],
        "División": resultados[3]
    }
    return diccionario_resultados

# Ejemplo de uso
a = float(input('Ingresa un número: '))
b = float(input('Ingrea otro número: '))
resultados = almacenar_resultados(a, b)
print(resultados)
