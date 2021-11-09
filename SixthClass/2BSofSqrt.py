##Ejercicio 2
# el siguiente codigo busca la raiz entera de un numero dado usando BS
# Busqueda Binaria
# Entrada:
# 16  (si se desea encontrar de un numero
#       mayor 20 incrementar el tamanio del array)
# Salida:
# Does not exist
#or
# "The element was found " +48
# 
# El ejercicio incluye el ordenamiento del array creado
# Autor:  Yeimy Huanca

def binarySearch(list ,n):
    baja = 0
    alta = len(list) - 1

    while baja <= alta:
        middle = (alta + baja) // 2
        middle_element = list[middle]
        cuadrado = middle_element*middle_element

        if cuadrado == n:
            return middle

        if cuadrado < n:
            baja = middle + 1
            
        else:
            alta = middle - 1

    
        
    return middle

def createList(n):
    lst = []
    for i in range(n+1):
        lst.append(i)
    return(lst)


#length = int(input("length: "))
#list = list(range(length, 0, -1))
n = int(input("search?: "))
list = createList(20)

#list = [1,5,9,7,15,19,20,40,48,50,90,91,100,150,151]

print(list)
#insertion_sort(list)
#print(list)

q= binarySearch(list, n)
if q == -1:
    print("Does not exist")
else:
    print("The element was found ",list[q])

