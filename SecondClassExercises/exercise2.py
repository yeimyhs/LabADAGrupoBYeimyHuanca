##Ejercicio 2
# el siguiente codigo recrea el pseudocodigo presentado en clase
# Busqueda secuencial
# Entrada:
# 3

# 6
# Salida:
# Does not exist

# The element was found
#
# Autor:  Yeimy Huanca

def sequetialSearch(list, n):
    find = 0
    for i in list:
        if i == n:
            find = 1
            break
        else:
            find = -1
    return find

list = [19, 4, 5, 6, 7, 56, 20, 30, 40]
n = int(input("search?: "))
find = sequetialSearch(list, n)

if find == 1:
    print("The element was found")
else:
    print("Does not exist")


