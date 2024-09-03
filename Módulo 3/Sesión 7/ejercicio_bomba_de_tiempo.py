import time

print('Bomba de tiempo a explotar')
i = 5
while i >= 0:
    print(i)
    i -= 1
    time.sleep(1)
    
print('Boom!')