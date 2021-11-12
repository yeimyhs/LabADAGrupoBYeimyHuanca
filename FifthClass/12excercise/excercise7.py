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
# la complejidad resultante es de Olog(n)
# ya que se tiene la siguiente induccion con respecto a su crecimiento
#   n, n/2, n/4, n/8, ... n/2^k 
#   1, 2, 4, 8, 16, ... 2^k 
#   por lo que i recorreria log(n)

# Autor:  Yeimy Huanca
  
n=5
j = 0         #Asignacion es  O(1)
i = 1        
while(j <= n): 
    i *= 2     
    j +=  1  
    print (i)   
     
print("2 ^",j ," = ", i)    
