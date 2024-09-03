#contador de vocales
def contar_vocales(texto):
    texto = texto.lower()
    vocales = 'aeiou'
    contador = 0
    for letra in texto:
        if letra in vocales:
            contador += 1
    return contador

cadena_usuario = input('Introduce una cadena de texto: ')
print(f"La cadena tiene {contar_vocales(cadena_usuario)} vocales")


#numero al azar
import random

azar = random.randint(1, 100)

while True:
    numero = int(input('ingrese un número entre 1 y 100: '))
    
    if numero == azar:
        print('Bien. Adivinaste el número')
        break
    elif numero > azar:
        print('El número que elegiste es mayor')
    elif numero < azar:
        print('El número que elegiste es menor')
