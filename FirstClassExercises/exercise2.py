##Ejercicio 2
# el siguiente codigo lee n números en un array y mostrarlos en orden inverso
# Entrada: 1 3 5 7 9
# Salida: 9 7 5 3 1
#
# Autor:  Yeimy Huanca
print("ejercicio2")
num =0
arr = []
print("Coloque'q'para parar.\nIngrese los numeros del array")
suma = 0
while num != "q":
  num=input()
  if num != "q" :
    num=int(num)
    arr.append(num)
print(arr)


for j in range(len(arr)) :
  print (arr[(j+1)*-1])
  #print (j*-1)