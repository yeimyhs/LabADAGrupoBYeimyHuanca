##Ejercicio 4  A Vicious Pikeman
# Pide cuanto tiempo tomara a un concursante de la edad media
#  resolver unos ejercicios. El problema nos pide encontrar la 
# cantidad maxima de ejercicios que puede resolver el  usuario 
# Concursante y la penalizacion que recibira al realizar los 
# ejercicios

# Autor:  Yeimy Huanca


#Casos de prueba ,colocar en consola----
#  
#input 1
'''
1 3
2 2 2 1
'''
#output 1
'''
1 1
'''

#input 2
'''
2 10
2 2 2 2
'''
#output 2
'''
2 4
'''

def solveProblems(n, givenTime, timeSolve):    
    totalTime, penalty = 0, 0           
    #variable del tiempo y penalizacion    
    for i, t in enumerate(timeSolve):   
        #iteramos en la lista          
        if (totalTime + t) > givenTime: 
            #si el tiempo total mas el tiempo que tardamos en resolver el ejercicio es mayor al tiempo maximo del concurso
            return i, penalty  
        #retorna la cantidad de ejercicios              
        totalTime += t  
        #agrega el tiempo de la iteracion               
        penalty = (penalty + totalTime) % 1000000007  
        # agrega el tiempo que ha pasado hasta resolver el ejercicio
    return n, penalty                   
    # retorna la cantidad de ejercicios resueltos y la penalizacion


n,t = map(int, input().split())       
a,b,c,t0 = map(int, input().split())                         
timeSolve = [t0]                     

for x in range(1, n):                 
    value = ((a * timeSolve[-1] + b) % c) + 1
    #calcula el tiempo de resolucion del ejercicio
    timeSolve.append(value)           
    #agrega el tiempo de resolucion del ejercicio a la lista
timeSolve = sorted(timeSolve)
#ordenamos los tiempos de resolucion de los ejercicios           
print(*solveProblems(n, t, timeSolve))