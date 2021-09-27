##Ejercicio 4
# el siguiente codigo lee 3 números y mostrarlos en orden ascendente
# Entrada: 9 5 8
# Salida: 5 8 9
#
# Autor:  Yeimy Huanca

def ordenamientoPorInsercion(unaLista):
   for indice in range(1,len(unaLista)):

     valorActual = unaLista[indice]
     posicion = indice

     while posicion>0 and unaLista[posicion-1]>valorActual:
         unaLista[posicion]=unaLista[posicion-1]
         posicion = posicion-1

     unaLista[posicion]=valorActual
     
print("ejercicio4")
num =0
arr= []
for indice in range(3):
  num=int(input())
  arr.append(num)

ordenamientoPorInsercion(arr)
print(arr)
