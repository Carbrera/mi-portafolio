suma = 3000 
contador = 0 
    
try:
    resultado = suma/contador
    print(resultado)
        
except ZeroDivisionError:
    print('División por cero')