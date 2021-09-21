#def ejercicio2(self):
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