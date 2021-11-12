##Ejercicio 4
# Cual es la complejidad del codigo?
# 
# Entrada:
# -
# Salida:
'''
Cuadrado de 1 1
Cuadrado de 2 4
Cuadrado de 2 4
Cuadrado de 3 9
Cuadrado de 3 9
Cuadrado de 3 9
Cuadrado de 4 16
Cuadrado de 4 16
Cuadrado de 4 16
Cuadrado de 4 16

'''
# la complejidad resultante es de O(n^2)
# ya que se tiene la siguiente induccion
#   # 1 + 2 + 3 + ... + n = n * (n + 1) / 2   
# y tambien porque el bucle for se aida dos veces
# Autor:  Yeimy Huanca
  
n=5
for i in range(0, n):                                 # n
    for j in range(0, i):                             # n*n
        if i == i:                                    # O(n)*n
            print("Cuadrado de", str(i), str(i*i))    # O(n)*n

