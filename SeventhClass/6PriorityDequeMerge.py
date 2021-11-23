##Ejercicio 6
# el siguiente codigo usa la estructura ya implementada para juntar listas de una lista
# al final obteniendo una lista ordenada de todos los elementos
#  
# Queues -ref https://docs.python.org/3/library/collections.html
import queue

# Entrada:
#                     Casos de prueba planteados  
# Salida:
# 
# PriorityQ process: []
# PriorityQ process: [1]
# PriorityQ process: [1, 4]
# PriorityQ process: [1, 4, 5]
# PriorityQ process: [1, 1, 5, 4]
# PriorityQ process: [1, 1, 5, 4, 3]
# PriorityQ process: [1, 1, 4, 4, 3, 5]
# PriorityQ process: [1, 1, 2, 4, 3, 5, 4]
# Output without order: [1, 1, 2, 4, 3, 5, 4, 6]
# Output in order: [1, 1, 2, 3, 4, 4, 5, 6]
#
# Autor:  Yeimy Huanca


#Casos de prueba descomentar para probar----
input =[[1,4,5],[1,3,4],[2,6]]

#input = ""
#-------------------------------------------

output=[]
priorityQueue = queue.PriorityQueue()
for i in input:
    for j in i: 
        print('# PriorityQ process:',priorityQueue.queue)
        priorityQueue.put(j)

print('Output without order:',priorityQueue.queue)
while not priorityQueue.empty():
    output.append(priorityQueue.get()) 
#print("# result: ---------------------------")
print('Output in order:',output)