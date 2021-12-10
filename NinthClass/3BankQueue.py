##Ejercicio 3  BankQueue
# Para una cola de banco se quiere atender a los cliente que generen mayor ganancia la banco 
# pero estos tienen un tiempo de tolentacia en la fila, 
# despues de este se iran; lo que se quiere es dar a conocer el valor maximo que ganara el banco.
#
# Entrada:
#                     Casos de prueba planteados  
# Autor:  Yeimy Huanca


#Casos de prueba ,colocar en consola----
#  
#input 1
'''
4 4
1000 1
2000 2
500 2
1200 0
'''
#output 1 → 4200

#input 2
'''
3 4
1000 0
2000 1
500 1
'''
#output 2 → 3000

#-------------------------------------------

import sys
#BANK QUEUE
def solution(dataCliente, numberPeople, totalTime):
    ## recibe una matriz , [0] dinero, [1] tiempo
     
    totalCash = 0                         
    # dineros total   
    waitingTime = 0                       
    # Tiempo de espera               
    
    select = [False]*totalTime            
    # Lista de tiempos de espera    
    
    while (waitingTime < numberPeople and not(len(dataCliente) == 0)): 
    # mientras el tiempo sea menor a la cantidad de clientes
              
        personActual = dataCliente[0]     
        # Obtenemos el cliente actual
        dataCliente.remove(dataCliente[0]) 
        # Eliminamos el cliente actual de la lista       
        start = personActual[1]           
        # Obtenemos el tiempo de inicio
              
        while(start >= 0 and select[start]): 
            # mientras el tiempo sea mayor a 0 y el tiempo de espera sea verdadero
            start -= 1                       
            # Decrementamos el tiempo de espera
            
        if(start != -1):                                 
            waitingTime += 1                 
            # Incrementamos el tiempo de espera
            select[start] = True             
            # Marcamos el tiempo de espera como verdadero            
            totalCash += personActual[0]     
            # Sumamos el dinero del cliente actual
            
    return totalCash                         
    # Retornamos el dinero total
    
def getInput(): return map(int, sys.stdin.readline().strip().split())  # ENTRADA DE DATOS    

customers = []                     
# Lista de clientes

n, t = getInput()
n = int(n)
t = int(t)


temListCustomers = []              
# Lista con los datos de los clientes
for line in range(n):               
    # Iteramos por cada cliente
    dinero, tiempo = getInput()     
    # Obtenemos los datos del cliente
    temListCustomers.append(dinero)
    temListCustomers.append(tiempo)
    ## Agregamos a la matriz
    customers.append(temListCustomers) 
    # Agregamos a la matriz
    temListCustomers = []

customers = sorted(customers, key=lambda item :(item[0], t - item[1]), reverse=True)  
# Ordenamos la lista de clientes / Ordenamos por dinero y tiempo/ inverso
print(solution(customers, n, t))