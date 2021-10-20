##Ejercicio 1   de N^2 a N
# el siguiente codigo recrea la funcion inicialmente dada de complejidad O(n^2)
# a complejidad O(n)
#
# Entrada:
# -
# Salida:
# greatest int
#
# Autor:  Yeimy Huanca
def greatestumberO_n2(array):
    for i in array:
        iValTheGreatest = True
        for j in array:
            if j>i:
                iValTheGreatest = False
        if iValTheGreatest:
            return i

def greatestNumberO_n(array):
    greatest = array[0]
    for i in array:
        if i > greatest:
            greatest = i
    return greatest
    

# caso de prueba
array = [9,13,2,0,17,23]
print(greatestNumberO_n(array))
