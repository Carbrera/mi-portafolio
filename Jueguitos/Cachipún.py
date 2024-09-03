import random

lista = ['Piedra', 'Papel', 'Tijeras']

empate = "Empate. Elige otra vez."
victoria = "¡Bien! ¡Ganaste!"
perdida = "Qué lástima. Perdiste."

while True:
    azar = random.choice(lista)

    cachi = input("Vamos a jugar al 'Cachipún'. Elige una de las siguientes opciones:\n"
        "1.- Piedra\n"
        "2.- Papel\n"
        "3.- Tijeras\n"
        "4.- Salir\n").lower() 
        
    print("Yo elegí",azar,".")
    
    match cachi:
        case '1' | 'piedra':
            print("Tú elegiste Piedra.")
            if azar == "Piedra":
                print(empate)
            elif azar == 'Papel':
                print(perdida)
            else:
                print(victoria)
        case '2' | 'papel':
            print("Tú elegiste Papel.")
            if azar == "Papel":
                print(empate)
            elif azar == 'Tijeras':
                print(perdida)
            else:
                print(victoria)
        case '3' | 'tijeras':
            print("Tú elegiste Tijeras.")
            if azar == "Tijeras":
                print(empate)
            elif azar == 'Piedra':
                print(perdida)
            else:
                print(victoria)
        case '4' | 'salir':
            print("Oh, bueno. En otra ocasión será.")
            break
        case _:
            print("Tu elección es inválida. Intenta de nuevo.")