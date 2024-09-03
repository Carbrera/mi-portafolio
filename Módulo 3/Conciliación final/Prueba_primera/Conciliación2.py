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

clasificacion = {
    "magos": ["Harry Houdini", "David Blaine", "Teller"],
    "cientificos": ["Newton", "Hawking", "Einstein"],
    "otros": []
}

for nombre in nombres:
    if nombre not in clasificacion["magos"] and nombre not in clasificacion["cientificos"]:
        clasificacion["otros"].append(nombre)

# Función para hacer grandiosos a los magos
def hacer_grandioso(magos):
    return ["El gran " + mago for mago in magos]

# Función para imprimir nombres
def imprimir_nombres(categoria, nombres):
    print(f"{categoria.capitalize()}:")
    for nombre in nombres:
        print(nombre)
    print("\n")

# Hacer grandiosos a los magos
clasificacion["magos"] = hacer_grandioso(clasificacion["magos"])

# Imprimir lista original
print("Lista original:")
imprimir_nombres("Todos", nombres)

# Imprimir resultados
imprimir_nombres("Magos grandiosos", clasificacion["magos"])
imprimir_nombres("Científicos", clasificacion["cientificos"])
imprimir_nombres("Otros", clasificacion["otros"])
