##Ejercicio 2  
# el siguiente codigo identifica los indices pares y suma los valores del arreglo
# sumandolos en esa posicion.

# Complejidad del algoritmo : O(n^2) por los dos for implementados uno dentro del otro
#
# Entrada:
# -
# Salida:
# all adds
#
# Autor:  Yeimy Huanca

def everyOther(array):                 
    for i in range(len(array)):         
        if i % 2 == 0:
            for j in array:            
                print(str(array[i])+ " + " + str(j) +" = " +str(array[i]+j))

array = [1,2,3,6,7]
everyOther(array) 