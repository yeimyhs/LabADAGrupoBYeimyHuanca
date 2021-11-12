##Ejercicio 11
# Cual es la complejidad del codigo?
# 
# Entrada:
# -
# Salida:
'''
si n 10 o 16
    primer while 2
    primer while 4
    primer while 8
    primer while 16
    segundo while 16
    segundo while 16
    -------------
    
'''
# 
#
# la complejidad resultante es de O log(log(n))

#  ya que es un efecto cadena, el primer buble ya lo resolvimos
#  y sale log(p), en el segundo bucle es la misma idea log(p), seria log(log(p))

# Autor:  Yeimy Huanca
  
n=16
p = 0
i = 1
while(i < n):   # O(log(n))      
    p = p + 1
    i = i * 2
    print ('primer while',i)

j = 1
while(j < p):   # O(log(log(n)))
    j = j * 2
    print ('segundo while',i)
      
