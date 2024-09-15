'''
Diseñe un programa en Python que agregue el siguiente contenido al archivo: informacion.dat. 

Hola Mundo  
Este en una nueva línea en el archivo 
agregando la segunda línea del archivo 
finalizando la línea agregada 

El nuevo archivo contiene la siguiente información: 

Datos de información en la línea 1 
Datos de información en la línea 2 
Datos de información en la línea 3 
Datos de información en la línea 4 
Datos de información en la línea 5 
Este en una nueva línea en el archivo 
agregando la segunda línea del archivo 
finalizando la línea agregada 
'''

def agregar_datos(nombre_archivo, lista):
    try:
        with open(nombre_archivo, 'a', encoding='utf-8') as file:
            for i in lista:
                file.write(i + '\n')
    except FileNotFoundError:
        print('Error: Archivo no encontrado')
        
lista = [
    'Hola Mundo',
    'Este en una nueva línea en el archivo',
    'agregando la segunda línea del archivo',
    'finalizando la línea agregada'
]

agregar_datos('informacion.dat', lista)