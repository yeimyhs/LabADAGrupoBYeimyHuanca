##Ejercicio 6
# Cual es la complejidad del codigo?
# 
#imprime la suma de numeros de 0 a i
# Entrada:
# -
# Salida:
# La suma de 1 a 4  es  10
# 
#
# la complejidad resultante es de O(n^(1/2))
# ya que se tiene la siguiente induccion
#   #  k       1 + 2 + 3 + 4 + ... + k
#      k > n
#   p = k * (k + 1) / 2         p > n       
#   k * (k + 1) / 2 > n
#   k^2 > n
#   k > sqrt(n) 
# y tambien porque el bucle for se aida dos veces
# Autor:  Yeimy Huanca
  
n=5
j = 0         #Asignacion es  O(1)
i = 1        
while(j <= n):     
    j +=  i     
    i += 1   
print("La suma de 1 a",i," es ", j + i)    
