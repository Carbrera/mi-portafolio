'''
Dada la siguiente lista de nombres: 
• Harry Houdini
• Newton
• David Blaine
• Hawking
• Messi
• Teller
• Einstein
• Pele
• Juanes
Y sabiendo que Harry Houdini, David Blaine y Teller son magos.
Y también que Newton, Hawking y Einstein son científicos.
Debemos separar los nombres en tres grupos: magos, científicos y otros; y escribir una función llamada hacer_grandioso(), que modifique la lista de magos añadiendo la frase ‘El gran‘ antes del nombre de cada mago.
Crear una función llamada imprimir_nombres(), que imprime el nombre de cada persona de la lista.
Finalmente, imprimir en pantalla la lista completa de nombres antes de ser modificados; luego imprimir los nombres de los magos grandiosos, los nombres de los científicos, y los restantes. 
'''

nombres = ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]

# separar nombres en tres grupos
def clasificar_nombres(nombres):
    magos = ["Harry Houdini", "David Blaine", "Teller"]
    cientificos = ["Newton", "Hawking", "Einstein"]
    otros = []

    for nombre in nombres:
        if nombre not in magos and nombre not in cientificos:
            otros.append(nombre)
                    
    return magos, cientificos, otros

#Función hacer_grandiosos
def hacer_grandioso(magos):
    for i in range(len(magos)):
        magos[i] = "El gran " + magos[i]

# Función para imprimir nombres
def imprimir_nombres(nombres):
    for nombre in nombres:
        print(nombre)

magos, cientificos, otros = clasificar_nombres(nombres)

# Imprimidores
print("Lista completa:")
imprimir_nombres(nombres)
print("\n")

hacer_grandioso(magos)

print("Magos grandiosos:")
imprimir_nombres(magos)
print("\n")

print("Científicos:")
imprimir_nombres(cientificos)
print("\n")

print("Otros:")
imprimir_nombres(otros)
