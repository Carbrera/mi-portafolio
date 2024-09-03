'''
En esta actividad trabajaremos con listas. Tomando la lista que se entrega a continuación, se solicita realizar las siguientes acciones en el orden indicado: 
1. Eliminar los elementos duplicados. 
2. Ordenar la lista resultante en orden ascendente.
'''

mi_lista = [5, 20, 15, 20, 25, 50, 20, 5, 18, 15]

mi_otra_lista = []

for i in mi_lista:
    if i not in mi_otra_lista:
        mi_otra_lista.append(i)
        
mi_otra_lista.sort()        

print(mi_otra_lista)

#----------------------------------------------------------------------------

mi_lista2 = []
mi_lista2 = mi_lista[0:1]
for i in range(len(mi_lista)):
    if mi_lista[i] not in mi_lista2:
        mi_lista2.append(mi_lista[i])
    print(mi_lista2)
    
#----------------------------------------------------------------------------
mi_lista = list(set(mi_lista)).sort()
mi_lista = sorted(list(set(mi_lista)))