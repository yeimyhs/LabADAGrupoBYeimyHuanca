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