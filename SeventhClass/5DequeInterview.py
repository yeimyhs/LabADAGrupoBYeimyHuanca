##Ejercicio 5
# el siguiente codigo usa la estructura ya implementada para identificar elementos y simbolos
# matematicos para realizar su respectivaoperacion
#  
# Queues -ref https://docs.python.org/3/library/collections.html
from collections import deque

# Entrada:
#                     Casos de prueba planteados  
# Salida:
# 
# Input: [4, -1, 5, 2, 3]
# Output: 9
#
# Autor:  Yeimy Huanca


#Casos de prueba descomentar para probar----
input = [4, -1, 5, 2, 3]

#input = ""
#-------------------------------------------
key = "#"
print('Input:',input)
deque = deque()
#print("# process: ---------------------------")   
output = 0
while True:
    if(input[0] < 0): 
        break
    elif(input[-1] < 0):
        break
    else:
        if(input[0] < input[-1]):
            output += input.pop(0)
        else:
            output += input.pop(-1)

#print("# result: ---------------------------")
print('Output:',output)