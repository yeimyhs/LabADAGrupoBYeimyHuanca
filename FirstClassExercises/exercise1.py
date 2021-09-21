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