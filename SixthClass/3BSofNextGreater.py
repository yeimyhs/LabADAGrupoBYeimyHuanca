##Ejercicio 2
# el siguiente codigo hace uso de el algoritmo de BS 
# para buscar el mayor inmediato o si existe el elemento retornar ese mismo
# 
# Busqueda Binaria
# Entrada:
# -                   (ejemplos ya propuestos)
# Salida:
# Does not exist
#or
# "The element was found " +el mayor inmediato
'''
Hallando mayor inmediato de :               18
The element was found  19
Hallando mayor inmediato de :               39
The element was found  40
Hallando mayor inmediato de :               4
The element was found  5
Hallando mayor inmediato de :               130
The element was found  150
Hallando mayor inmediato de :               70
The element was found  70
Hallando mayor inmediato de :               80
The element was found  91

'''
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

        if middle_element < n:
            baja = middle + 1
            
        if middle_element > n:
            alta = middle - 1

    return middle+1

def createList(n):
    lst = []
    for i in range(n+1):
        lst.append(i)
    return(lst)


#length = int(input("length: "))
#list = list(range(length, 0, -1))
n =[18,39,4,130,70,80]#int(input("search?: ")) # 
list = createList(20)

list = [1,5,7,9,15,19,20,40,48,50,70,91,100,150,151]

print(list)
#insertion_sort(list)
#print(list)
for i in n:
    print('Hallando mayor inmediato de :              ',i)
    q= binarySearch(list, i)
    if q == -1:
        print("Does not exist")
    else:
        print("The element was found ",list[q])

