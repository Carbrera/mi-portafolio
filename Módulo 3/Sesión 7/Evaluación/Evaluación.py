'''
Se debe imprimir cada dato de las listas en pantalla con las siguientes excepciones:  
• Filtra y muestra únicamente los estudiantes que tienen más de 18 años y cuyo promedio de calificaciones sea superior a 85. 
• Calcula el promedio de las calificaciones de los estudiantes que tienen más de 18 años y cuya edad sea un número primo. 
'''
# Definimos el cálculo de números primos
def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Definimos el calculo de los promedios
def promedio(lista):
    return sum(lista) / len(lista)    

# Lista de estudiantes
estudiantes = [
    {'nombre': 'Juan', 'edad': 17, 'calificaciones': [85, 90, 88]}, 
    {'nombre': 'María', 'edad': 19, 'calificaciones': [92, 89, 90]},
    {'nombre': 'Pedro', 'edad': 21, 'calificaciones': [85, 95, 80]}, 
    {'nombre': 'Ana', 'edad': 18, 'calificaciones': [90, 92, 87]}, 
    {'nombre': 'Luis', 'edad': 20, 'calificaciones': [88, 85, 92]}, 
] 

# Filtra y muestra únicamente los estudiantes que tienen más de 18 años y cuyo promedio de calificaciones sea superior a 85.
print('--Estudiantes mayores de 18 y con promedio superior a 85: ')
estudiantes_filtrados = []
for estudiante in estudiantes:
    if estudiante['edad'] > 18 and promedio(estudiante['calificaciones']) > 85:
        estudiantes_filtrados.append(estudiante)
        print(estudiante['nombre'])


# Calcula el promedio de las calificaciones de los estudiantes que tienen más de 18 años y cuya edad sea un número primo.
print('--Estudiante mayor de 18 cuya edad es un número primo y su promedio: ')        
for estudiante in estudiantes_filtrados:
    if es_primo(estudiante['edad']):
        print(f'{estudiante['nombre']}: ')
        print(f'Promedio de calificacion {promedio(estudiante['calificaciones'])}')