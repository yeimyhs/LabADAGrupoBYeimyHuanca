##Ejercicio 5  Watering Grass
# Se instalan aspersores "n" en una franja horizontal de césped de "l" 
# metros de largo y "w" metros de ancho. Cada rociador se instala en 
# la línea central horizontal de la tira. Para cada rociador se nos da 
# su posición como la distancia desde el extremo izquierdo de la línea 
# central y su radio de operación.
# ¿Cuál es el número mínimo de aspersores que se deben encender para regar
#  toda la franja de césped?
# Autor:  Yeimy Huanca


#Casos de prueba ,colocar en consola----
#  
#input 1
'''
8 20 2
5 3
4 1
1 2
7 2
10 2
13 3
16 2
19 4
3 10 1
3 5
9 3
6 1
3 10 1
5 3
1 1
9 1
'''
#output
'''
6
2
-1
'''

import sys
from math import sqrt


def solution(aspersores, l, n):
    useAmount, currentSprinkler, currentLen = 0, 0, 0 
    # aspersores usados, aspersor actual, largo de la franja 
    
    while True:  
        # itera hasta que toda la franja este regada
        masAlejado = -1  
        
        while currentSprinkler < n and aspersores[currentSprinkler][0] <= currentLen: 
            # mientras haya aspersores y la longitud del aspersor actual no sea mayor a la longitud regada por otros aspersores
            masAlejado = max(masAlejado, aspersores[currentSprinkler][1]) 
            # actualiza el aspersor mas alejado
            currentSprinkler += 1                           
            # avanzamos al siguiente aspersor                

        if masAlejado == -1:                                 
            # Si no se pudo regar la franja con los aspersores que tenemos devolvemos -1
            return -1
        useAmount += 1
        currentLen = masAlejado
        # actualizamos la longitud regada
        
        if currentLen >= l:                                  
            # Si se rego la franja devolvemos el numero de aspersores usados
            return useAmount
                                
lines = 0             
for line in sys.stdin:          
    if lines == 0:
        n, l, w = map(int, line.split())
        aspersores = []
        lines = n 
    else:
        lines -= 1  
        h, r = map(int, line.split()) 
        if (2 * r) > w: 
            d = sqrt((r ** 2) - ((w / 2) ** 2))
            # calcula la distancia del aspersor al centro de la franja
            aspersores.append((h - d, h + d))         
            # agrega el aspersor a la lista de aspersores
        if lines == 0:  
            aspersores = sorted(aspersores) 
            print(solution(aspersores, l, len(aspersores))) 