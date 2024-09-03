suma = 0

while True:
    num = int(input('Ingrese un número positivo para sumar: '))
    if num < 0:
        print('No se permiten números negativos.')
        break
    suma += num
    print(f'El total de la suma es: {suma}')