##Ejercicio 8
# Cual es la complejidad del codigo?
# 
# Entrada:
# -
# Salida:
'''
    2.5
    1.25
    0.625
'''
# 
#
# la complejidad resultante es de Olog(n)
# ya que i tiene la forma (n/2^k)
# y para que se rompa la condicion k tiene que ser log(n)
#  # Assume that i < 1
# Therefore n / 2^k < 1
#           n / 2^k = 1
#                 n = 2^k
#                 k = log(n)
# A8: O(log(n))

# Autor:  Yeimy Huanca
  
n=5
i = n
while(i >= 1):
    i = i/2
    print(i)
      
