'''Partiendo del ejercicio anterior (Rebound Exercises), construya una función que reemplace el contenido de “Información” por “Procesamiento”, e imprima cuántos reemplazos realizó en el archivo.
Teniendo como salida lo siguiente: 

$ $ python ejercicio.py  
Se realizaron: 5 remplazos 

El contenido del archivo informacion.dat es: 

Datos de Procesamiento en la línea 1 
Datos de Procesamiento en la línea 2 
Datos de Procesamiento en la línea 3 
Datos de Procesamiento en la línea 4 
Datos de Procesamiento en la línea 5 
Este en una nueva línea en el archivo 
agregando la segunda línea del archivo 
finalizando la línea agregada 
'''

def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as file:
            datos = file.readlines()
            return datos
    except FileNotFoundError:
        print('Error: Archivo no existe')

def cambiar_palabra(palabra_existente, palabra_nueva, lista):
    lista_nueva = []
    contador_palabras = 0
    for i in lista:
        if palabra_existente in i:
            #'Datos de información en la línea 1\n'.strip().replace('información', 'procesamiento')
            lista_nueva.append(i.strip().replace(palabra_existente, palabra_nueva))
            contador_palabras += 1
        else:    
            lista_nueva.append(i.strip())                   
    return lista_nueva           
 
def escribir_archivo(lista, nombre_archivo):
    try:
        with open(nombre_archivo, 'w', encoding='utf-8') as file:
            for i in lista:
                file.write(i + '\n')
    except FileNotFoundError:
        print('Error: Archivo no existe')
                    
lista_datos = leer_archivo('informacion.dat')
lista_datos_reemplazados = cambiar_palabra('información', 'procesamiento', lista_datos)
escribir_archivo(lista_datos_reemplazados, 'informacion.dat')