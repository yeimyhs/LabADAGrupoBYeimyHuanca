##Ejercicio 1
# el siguiente codigo lee n números en un array y retornar la suma de los mismos
# Entrada: 1 2 3 4 
# Salida: 10
#
# Autor:  Yeimy Huanca

print("ejercicio1")
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

for j in arr:
  suma += j
print (suma)