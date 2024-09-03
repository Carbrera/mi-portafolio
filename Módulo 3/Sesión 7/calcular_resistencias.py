'''
Calculo resistencia
Enunciado: Calcular la resistencia total dado el ingreso de 3 resistencias por consola rt = 1/((1/r1) + (1/r2) + (1/r3))
'''
def test_ingreso() :
    
    while True:
        
        try:
            
            r = float(input('Ingrese el valor de la resistencia: '))
            if r > 0 :
                return r
            else :
                print('La resistencia ingresada es negativa')
        except Exception as error:
            print('Ha sucedido un error en el ingreso de la resistencia.', error)

resis = int(input('Ingrese cuántas resistencias quiere calcular: '))

i = 0
lista = []
while i < resis:
    r = test_ingreso()
    lista.append(r)
    i += 1
    
resis_tot = 1/sum(1/r for r in lista)

print(resis_tot)   
    
#r1 = test_ingreso()
#r2 = test_ingreso()
#r3 = test_ingreso()

#rt = 1/((1/r1) + (1/r2) + (1/r3))

#print(f'{rt:.2f}')