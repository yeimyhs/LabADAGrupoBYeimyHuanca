##Ejercicio 4(exercise2 version Tiempo)
# el siguiente codigo recrea el pseudocodigo presentado en clase
# con medicion del tiempo de ejercion  con respecto a la cantidad de datos
# Busqueda secuencial
# Entrada:
# 3

# 6
# Salida:
# Does not exist

# The element was found
#
# Autor:  Yeimy Huanca
import time

def sequetialSearch(list, n):
    find = 0
    for i in list:
        if i == n:
            find = 1
            break
        else:
            find = -1
    return find

length = int(input("length: "))
list = list(range(length, 0, -1))
n = int(input("search?: "))

tik = time.perf_counter() 
find = sequetialSearch(list, n)
tak = time.perf_counter() 

if find == 1:
    print("The element was found")
else:
    print("Does not exist")

print(f"time of execute: {tak - tik:0.4f} seconds")
