##Ejercicio 1
# el siguiente codigo recrea el pseudocodigo de la busqueda binaria
# Busqueda Binaria
# Entrada:
# 48
# Salida:
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

