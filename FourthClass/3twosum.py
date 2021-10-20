##Ejercicio 2  
# el siguiente codigo identifica si existe alguna suma entre dos elementos
# distintos dentro de la listta , que sumen 10.

# Complejidad del algoritmo : O(n^2) por los dos for implementados uno dentro del otro
#
# Entrada:
# -

#Si hay entonces
# Salida:
# Son: 2 + 8 = 10
# True

#Si no
# Salida:
# False

# Autor:  Yeimy Huanca

def twoSum(array):
  for i in range(len(array)):                       
    for j in range(len(array)):                     
      if i != j and  (array[i] + array[j] == 10):   
        print("Hay al menos 2 numeros que suman 10") 
        print("Son: "+ str(array[i]) + " + " + str(array[j])+ " = 10")
        return True                                                                
  return False  

  # Caso de prueba
array = [1,4,3,8,5]
print(twoSum(array))