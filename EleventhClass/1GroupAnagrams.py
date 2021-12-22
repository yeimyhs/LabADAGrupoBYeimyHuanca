##Ejercicio 1
# Se tiene un arreglo de Strings que contienen un grupo de
# anagramas dentro del mismo. Un grupo de anagramas esta
# conformado por aquellas palabras que poseen las mismas
# letras pero en diferente orden ademas de tener la misma
# cantidad de repeticiones o frecuencias de letras usadas
# 
# Entrada:
#                     Casos de prueba planteados  
# Autor:  Yeimy Huanca


#Casos de prueba descomentar para probar----
strs = ["eat","tea","tan","ate","nat","bat"]
#strs = [""]
#strs = ["a"]

#outputs
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Output: [[""]]
# Output: [["a"]]
#-------------------------------------------

def solution(strs):
    # el metodo sorted ordena y devuelve una cadena,
    # mediante join agrupomos la palabras en una cadena vacia
    diccionarioWord = {}; 
    for i in strs:
        sortWord =  "".join(sorted(i))
        if sortWord not in diccionarioWord: 
            # si no estan en el diccionario
            diccionarioWord[sortWord] = [i] 
            #crea la variable
        else:
            diccionarioWord[sortWord].append(i) 
            # si la existe la variable agegamos elementos

    listadeLista = []
    for i in diccionarioWord.values(): 
        #para cada values en diccionario
        listadeLista.append(i) 
        #se ingresa en la listadeLista

    return listadeLista 


print(solution(strs))