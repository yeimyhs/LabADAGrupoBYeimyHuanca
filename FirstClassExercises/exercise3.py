##Ejercicio 3
# el siguiente codigo lee n números en un array y mostrarlos en orden inverso
# Entrada: 1 3 5 7 9
# Salida: 9 7 5 3 1
#
# Autor:  Yeimy Huanca
print("ejercicio3")
num =0
print("Coloque'q'para parar.\nIngrese los numeros")
pares= []
impares= []
while num != "q":
  num=input()
  if num != "q" :
    num=int(num)
    if num%2 == 0:
      pares.append(num)
    else:
      impares.append(num)
print("pares: ",pares)
print("impares: ",impares)