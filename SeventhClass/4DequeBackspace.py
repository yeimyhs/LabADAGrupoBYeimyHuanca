##Ejercicio 3
# el siguiente codigo usa la estructura ya implementada para identificar elementos y simbolos
# matematicos para realizar su respectivaoperacion
#  
# Queues -ref https://docs.python.org/3/library/collections.html
from collections import deque

# Entrada:
#                     Casos de prueba planteados  
# Salida:
# 
# process: ---------------------------
# Deque deque(['a', 'b'])
# Deque deque(['a', 'b', 'd'])
# Deque deque(['a', 'b'])
# Deque deque(['a', 'b'])
# Deque deque(['a', 'b', 'g', 'h'])
# Deque deque(['a', 'b', 'g', 'h', 'j', 'k', 'l', 'm'])      
# Deque deque(['a', 'b', 'g', 'h', 'j', 'k', 'l', 'm', 'o']) 
# Result: ---------------------------
# Input: abc#de##f#ghi#jklmn#op#
# Output: abghjklmo
#
# Autor:  Yeimy Huanca


#Casos de prueba descomentar para probar----
input = "abc#de##f#ghi#jklmn#op#"
#input = ""
#-------------------------------------------
key = "#"
deque = deque()
print("# process: ---------------------------")   
for i in input:
    if len(deque)>0 : 
        if i == "#":                            
            deque.pop() 
            print("# Deque",deque)              
        else:                                    
            deque.append(i)              
    else:                                   
        deque.append(i)
output = ""

for i in range(len(deque)):         
    output = output + str(deque.popleft())
print("# Result: ---------------------------")

print('Input:',input)
print('Output:',output)