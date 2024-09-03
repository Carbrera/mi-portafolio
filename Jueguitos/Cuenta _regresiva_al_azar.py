import random
import time

azar = random.randint(0,10)

print('Cuando esta cuenta regresiva al azar llegue a 0 serás electrocutado.')

while True:
    if azar == 0:
        print('La cuenta llegó a 0 \n"Bzzzzzt". Moriste.')
        break
    else:
       print("La cuenta regresiva va en",azar)
       azar = random.randint(0,10)
       time.sleep(1)
       