palabra = 'paralelepípedo'

patron = 'aeiouáéíóú'

consonantes = ''

for i in range(len(palabra)):
    if palabra[i] not in patron:
        consonantes += palabra[i]
    print(f'La letra {palabra[i]} se encuentra en la posición {i}')
    
print(f'Las letras consonantes son {consonantes}')


