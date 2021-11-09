##Ejercicio 1
# el siguiente codigo recrea el pseudocodigo de la busqueda binaria
# Busqueda Binaria
# Entrada:
# length: 48                    (tamanio del array a probar)
# search?: 48                   (elemento a buscar)
# Salida:
#array sin ordenar , inicial
''' [48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1] '''
#array ordenado
''' [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]'''
# Does not exist
#or
# "The element was found " +48
# 
# El ejercicio incluye el ordenamiento del array creado
# Autor:  Yeimy Huanca
def insertion_sort(array):
    for index in range(1, len(array)):
        currentValue = array[index]
        currentPosition = index

        while currentPosition > 0 and array[currentPosition - 1] > currentValue:
            array[currentPosition] = array[currentPosition -1]
            currentPosition = currentPosition - 1

        array[currentPosition] = currentValue

def binarySearch(list ,n):
    baja = 0
    alta = len(list) - 1

    while baja <= alta:
        middle = (alta + baja) // 2
        middle_element = list[middle]

        if middle_element == n:
            return middle

        if middle_element > n:
            alta = middle - 1
        else:
            baja = middle + 1
    return -1


length = int(input("length: "))
list = list(range(length, 0, -1))

n = int(input("search?: "))
#list = [1,5,9,7,15,19,20,40,48,50,90,91,100,150,151]
print(list)
insertion_sort(list)
print(list)

q= binarySearch(list, n)
if q == -1:
    print("Does not exist")
else:
    print("The element was found ",list[q])

