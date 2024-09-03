import random

# Definir las opciones
PIEDRA, PAPEL, TIJERAS = 'Piedra', 'Papel', 'Tijeras'
OPCIONES = [PIEDRA, PAPEL, TIJERAS]

# Diccionario para determinar el ganador
RESULTADOS = {
    (PIEDRA, TIJERAS): "¡Bien! ¡Ganaste!",
    (PAPEL, PIEDRA): "¡Bien! ¡Ganaste!",
    (TIJERAS, PAPEL): "¡Bien! ¡Ganaste!",
    (PIEDRA, PAPEL): "Qué lástima. Perdiste.",
    (PAPEL, TIJERAS): "Qué lástima. Perdiste.",
    (TIJERAS, PIEDRA): "Qué lástima. Perdiste."
}

# Mensajes
EMPATE = "Empate. Elige otra vez."
SALIR = "Oh, bueno. En otra ocasión será."

while True:
    # Elección de la computadora
    eleccion_pc = random.choice(OPCIONES)

    # Entrada del usuario
    eleccion_usuario = input("Vamos a jugar al 'Cachipún'. Elige una de las siguientes opciones:\n"
                             "1.- Piedra\n"
                             "2.- Papel\n"
                             "3.- Tijeras\n"
                             "4.- Salir\n").lower()

    if eleccion_usuario == '4' or eleccion_usuario == 'salir':
        print(SALIR)
        break

    # Mapeo de entrada del usuario a opciones válidas
    if eleccion_usuario in ['1', 'piedra']:
        eleccion_usuario = PIEDRA
    elif eleccion_usuario in ['2', 'papel']:
        eleccion_usuario = PAPEL
    elif eleccion_usuario in ['3', 'tijeras']:
        eleccion_usuario = TIJERAS
    else:
        print("Tu elección es inválida. Intenta de nuevo.")
        continue

    # Resultado
    print(f"Tú elegiste {eleccion_usuario}.\nYo elegí {eleccion_pc}.")
    if eleccion_usuario == eleccion_pc:
        print(EMPATE)
    else:
        print(RESULTADOS.get((eleccion_usuario, eleccion_pc), "Qué lástima. Perdiste."))
