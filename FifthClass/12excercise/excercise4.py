##Ejercicio 4
# Cual es la complejidad del codigo?
# 
# Entrada:
# -
# Salida:
'''
    0 x5 veces

    0
    1
    2
    3
    4

    0
    2
    4
    6
    8
                                        5^2 datos
    0
    3
    6
    9
    12

    0
    4
    8
    12
    16

'''
# la complejidad resultante es de O(n^2)
# ya que se tienen dos for anidados
#
# Autor:  Yeimy Huanca
  
n=5
for i in range(0, n):                             # n
    for j in range(0, n):                         # n^2
        print(i*j)                                # O(1)* n^2

