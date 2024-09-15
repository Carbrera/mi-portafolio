'''
Partiendo de la actividad realizada en el Rebound Exercises, construya una función que lea el contenido del archivo informacion.dat. 
Teniendo como salida lo siguiente: 

$ python ejercicio.py  
El archivo informacion.dat ya existe, ha sido creado previamente 
Datos de información en la línea 1 
Datos de información en la línea 2 
Datos de información en la línea 3 
Datos de información en la línea 4 
Datos de información en la línea 5 
'''

def crear_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'x') as file:
            file.write()
    except FileExistsError:
        print('El archivo informacion.dat ya existe, ha sido creado previamente')

def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as file:
            datos = file.readlines()           
            for i in datos:
                print(i)
    except FileNotFoundError:
        print('Error: Archivo no existe.')

crear_archivo('informacion.dat')        
leer_archivo('informacion.dat')