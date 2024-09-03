'''
Escribir un programa que analice un número, e indique si es positivo o negativo, y si es par o impar. En caso de ser cero, también indicarlo. Se debe usar la expresión if-elif-else, y no usar subcondiciones; en su lugar, usar condiciones anidadas. 
'''       
        
# Solicitar al usuario que ingrese un número
num = int(input("Introduce un número a evaluar: "))

# Verificar si el número es cero
if num == 0:
    print("El número es cero.")
else:
    # Determinar si es positivo o negativo
    if num > 0:
        print("El número ingresado es positivo.")
    else:
        print("El número ingresado es negativo.")
    
    # Determinar si es par o impar
    if num % 2 == 0:
        print("El número es par.")
    else:
        print("El número es impar.")