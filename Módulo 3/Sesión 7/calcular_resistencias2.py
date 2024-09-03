'''Calculo resistencia
Enunciado: Calcular la resistencia total dado el ingreso de 3 resistencias por consola rt = 1/((1/r1) + (1/r2) + (1/r3))'''

def calcular_resistencia_total():
    try:
        cantidad_resistencias = int(input("Introduce la cantidad de resistencias: "))
        
        resistencias = []
        
        for i in range(cantidad_resistencias):
            r = float(input(f"Introduce el valor de la resistencia R{i+1}: "))
            if r <= 0:
                raise ValueError(f"La resistencia R{i+1} debe ser un número mayor a 0.")
            resistencias.append(r)
        
        rt = 1 / sum(1 / r for r in resistencias)
        print(f"La resistencia total es: {rt} ohmios")

    except ValueError as ve:
        print(f"Error: {ve}")
    
    except Exception as ex:
        print(f"Error inesperado: {ex}")

calcular_resistencia_total()