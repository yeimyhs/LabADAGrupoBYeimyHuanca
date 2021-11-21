##Ejercicio 3
# el siguiente codigo usa la estructura ya implementada para identificar elementos y simbolos
# matematicos para realizar su respectivaoperacion
#  
# Queues -ref https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-queues
from collections import deque

# Entrada:
#                     Casos de prueba planteados  
# Salida:
# 
# process: ---------------------------
# Queue deque(['a'])
# Queue deque(['a', 'b'])
# Queue deque(['a', 'b', 'c'])
# Queue deque(['d'])
# Queue deque(['D', 'E'])
# Queue deque(['D', 'E', 'F'])
# Queue deque(['g'])
# Result: ---------------------------
# Input: abc$d@ef$@g$
# Output: abcDEFg
#
# Autor:  Yeimy Huanca


#Casos de prueba descomentar para probar----
input = "abc$d@ef$@g$"
#input = ""
#-------------------------------------------
stack = [] 
output = "" 
ctrlMayus = None                      
queue = deque()                   
buffer = ""                           
print("# process: ---------------------------")                       
for i in input:                        
    if i not in  "@$":                  
        if ctrlMayus == None:            
            queue.append(i) 
            print('# Queue',queue)            
        elif ctrlMayus == False:          
            queue.append(i.lower()) 
            print('# Queue',queue)    
        else:                             
            queue.append(i.upper())
            print('# Queue',queue) 
    else:                              
        if i == "$":                      
            buffer = queue.copy()      
            queue.clear()             
            output = output + "".join(buffer)   
        elif i == "@" and ctrlMayus == True:      
            queue = deque([x.lower() for x in queue]) 
            ctrlMayus = False
        elif i == "@" and (ctrlMayus == False or ctrlMayus == None): 
            queue = deque([x.upper() for x in queue])            
            ctrlMayus = True     
print("# Result: ---------------------------")
print('Input:',input)
print('Output:',output)
