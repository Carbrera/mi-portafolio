'''
Diseñe un programa en Python que cree un archivo si no se encuentra; en caso de existir el archivo, debe reflejar un mensaje que especifica que ya se encuentra el archivo previamente creado.
El archivo por crear debe llamarse informacion.dat. el cual contiene lo siguiente: 
Datos de información en la línea 1 
Datos de información en la línea 2 
Datos de información en la línea 3 
Datos de información en la línea 4 
Datos de información en la línea 5 
'''

def crear_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'x') as file:
            file.write('')
    except FileNotFoundError:
        print("Error: El archivo ya existe.")
        

def escribir_archivo(lista, nombre_archivo):
    try:
        with open(nombre_archivo, 'w', encoding='utf-8') as file:
            for i in lista:
                file.write(i + '\n')
    except FileNotFoundError:
        print('Error: Archivo no existe.')
        
lista = [
    'Datos de información en la línea 1',
    'Datos de información en la línea 2',
    'Datos de información en la línea 3',
    'Datos de información en la línea 4',
    'Datos de información en la línea 5'
]       

crear_archivo('informacion.dat')
escribir_archivo(lista, 'informacion.dat')