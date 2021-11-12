##Ejercicio 11
# Cual es la complejidad del codigo?
# 
# Entrada:
# -
# Salida:
'''
    10
'''
# 
#
# la complejidad resultante es de O(nlog(n))

#  ya que el primero solo depende de 'n', entonces el coste es 'n'
#  y el segundo tambien depende de 'n', pero el crecimiento es de log2(n)

# Autor:  Yeimy Huanca
  
n=10
i = 0
while(i < n):               # O(n)
    j = 1
    while(j < n):          # O(log n)
        j = j * 2
    i = i + 1

print (i)
      
