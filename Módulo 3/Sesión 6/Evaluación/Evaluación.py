num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))

# Evaluar las posibles combinaciones
if num1 > num2 and num1 > num3:
    if num2 > num3:
        print(f"El orden es: {num1}, {num2}, {num3}")
    else:
        print(f"El orden es: {num1}, {num3}, {num2}")
elif num2 > num1 and num2 > num3:
    if num1 > num3:
        print(f"El orden es: {num2}, {num1}, {num3}")
    else:
        print(f"El orden es: {num2}, {num3}, {num1}")
else:  # Si num3 es el mayor
    if num1 > num2:
        print(f"El orden es: {num3}, {num1}, {num2}")
    else:
        print(f"El orden es: {num3}, {num2}, {num1}")