##Ejercicio 3
# Cual es la complejidad del codigo?
# 
# Entrada:
# -
# Salida:
'''
    0
    2
    4
    6
    8

'''
# Lo que evidencia que la complejidad de ese for es de n
# O(n/2)pero los multiplos naturales no causan mayor efecto en la complejidad por lo que
# la complejidad resultante es de O(n)
#
# Autor:  Yeimy Huanca
  
n=10
for i in range(0, n, 2):  # n/2
    print (i)             # n/2

