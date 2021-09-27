##Ejercicio 1
# el siguiente codigo lee dos números enteros positivos nk (n, k <= 10 7 ) 
# Escriba un solo entero a la salida, denotando cuántos enteros t i son divisibles por k.
# Entrada:
# 7 3
# 1
# 51
# 966369
# 7
# 9
# 999996
# 11
# Salida:
# 4
#
# Autor:  Yeimy Huanca

def rectrictions(n , rectriction):
    while n >= rectriction:
	    n = int(input("Sobrepasa la restriccion  ::"))
    return n


rectriction = 10**7
rectrictionNum = 10**9
n = int(input(":"))
n = rectrictions(n, rectriction)
k = int(input(":"))
k = rectrictions(k, rectriction)
print( n ,k)
cant = 0

for i in range(n):
    num = int(input(" -."))
    num = rectrictions(num, rectrictionNum)
    if num % k == 0:
        cant += 1

print (cant)

