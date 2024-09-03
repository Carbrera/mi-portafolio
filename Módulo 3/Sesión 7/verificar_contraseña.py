'''
Buscar pass
Enunciado: Solicita al usuario ingresar una contraseña hasta que la contraseña 
ingresada coincida con una contraseña predefinida
'''

passw = '1234'



while True:
    var = input('Ingrese contraseña: ') # esta petición debe ir dentro del while o entrará en bucle
    if var == passw:
        print('Acceso concedido')
        break
    else :
        print('Acceso denegado')
        
    