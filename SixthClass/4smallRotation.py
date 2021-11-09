##Ejercicio 4
# el siguiente codigo retorna el minimos en un arreglo que se roto
# Busqueda Binaria
# Entrada:
# -                   (ejemplos ya propuestos)
# Salida:
# 4                    (es el menor primer ejemplo)
# 1                    (es el menor   segundo ejemplo)

# 
# Autor:  Yeimy Huanca

def binarySearch(list):
    baja = 0
    alta = len(list) - 1
    middle = (baja + alta) // 2    
    aux = 0          
    while baja <= alta:         
            
        middle = (baja + alta) // 2      
        
        if(list[baja] < list[middle] ):  
            aux =list[baja]          
            baja = middle            
        
        elif list[middle] < aux :  
            aux = list[middle] 
            alta = middle
        else:       
            baja = baja + 1
    return aux
list= [10,11,12,15,18,20,30,4,6,7,8,9]
print(binarySearch(list))


list= [10,11,12,15,18,20,30,1,2,4,6,7,8,9]
print(binarySearch(list))