'''
Son colecciones de datos que se pueden modificar
El acceso a los elementos de la tupla es por índices
Se definen con paréntesis ()
Se pueden definir con la función tuple()
'''
tupla = tuple()
tupla = ()
num = 1,2,3,4,5
print(tupla)
print(num)

# Índices van desde 0 a n-1
# Permite índices negativos
tupla = (40, 1.80, 'Fulanito', 'Perez')

# Acceder a la longitud de la tupla
print('La longitud de la tupla es: ', len(tupla))

# Acceder a un elemento mediante índice
print('El primer elemento de la tupla es: ', tupla[0])
print('El último elemento de la tupla es: ', tupla[-1])

# Contar elementos de una tupla
print('Elementos número 40 existentes: ', tupla.count(40))

# Obtener el índice de un elemento
print('El índice del elemento 40 es: ', tupla.index(40))

# desempaquetar tuplas
# Genera error ValueError: too many values to unpack, si existen menos o mas elementos que variables
a, b, c, d, e = num

# a = num[0]
print(f'a:{a}, b:{b}')

# crear una tupla de otra tupla
# otra_tupla = tupla
          # (40, 1.80, 'Fulanito', 'Perez')  
sub_tupla = tupla[0:3]
print('Sub tupla', sub_tupla)
print(tupla[2:]) # desde el indice 2 hasta el final
print(tupla[:-1])  # desde el principio hasta el penultimo
print(tupla[0:4:2])  # desde el indice 0 hasta el indice 3, con saltos de 2 en 2

# [inicio:final:paso]
# (inicio,final,paso)