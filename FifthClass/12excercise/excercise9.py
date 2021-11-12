##Ejercicio9
# Cual es la complejidad del codigo?
# 
# Entrada:
# -
# Salida:
'''
    Cuadrado de  1 1
    Cuadrado de  2 4
    Cuadrado de  3 9
    Cuadrado de  4 16
'''
# 
#
# la complejidad resultante es de O sqrt(n)

# dado que el comportamiento se da 0, 1, 4, 9, 16, i^k
# y dependiendo a n 0 , 1 ,4 ,9  16
#                   0   1  2  3  4
#recorreria  sqrt(n) veces por lo que resultaria en O sqrt(n)
# Autor:  Yeimy Huanca
  
n=16
i = 0
while(i*i < n):
    i = i + 1    
    print("Cuadrado de ",i,i*i) 
      
