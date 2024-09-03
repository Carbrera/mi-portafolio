'''
Realizar cálculo de la hipotenusa requiriendo el ingreso del cateto a y el cateto b por parte del usuario
'''

a = int(input('Ingresa el valor del lado a: '))
b = int(input('Ingresa el valor del lado b: '))


hipotenusa = (a**2 + b**2) **0.5
print(hipotenusa)