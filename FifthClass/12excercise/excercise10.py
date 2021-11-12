##Ejercicio 10
# Cual es la complejidad del codigo?
# 
# Entrada:
# -
# Salida:
'''
i*2
    0
    2
    4
    6
    8
    10
    12
    14
    16
    18
    -------------
i*3
    0
    3
    6
    9
    12
    15
    18
    21
    24
    27
'''
# 
#
# la complejidad resultante es de O (n)

# dado que se presentan dos for de complejidadn cada uno
# seria O(2n) sin embargo los naturales que multiplican o dividen no hacer mayor efecto por lo que
# unicamente resultaria en O(n)
# Autor:  Yeimy Huanca
  
n=10
for i in range(n):
    print(i*2)          # On
print('-------------')
for j in range(n):
    print(j*3)          # On
      
