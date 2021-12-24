##Ejercicio 5
# En este rompecabezas, se muestran 7 letras en una disposición hexagonal
# de 6 letras alrededor de una letra central.
# La tarea consiste en crear el mayor número posible de palabras que:
# - contengan sólo las letras que se muestran en el hexágono,
# - tengan al menos una longitud de 4, y
# - contengan la letra central.
# Una letra puede utilizarse más de una vez, y no es necesario utilizar todas las letras
# tienen que usarse todas las letras.

# 
# Entrada:
#                     Casos de prueba planteados  
# Autor:  Yeimy Huanca


#Casos de prueba (copiar en consola)
'''
drulyag
27
dryad
duly
spelling
multiplexed
janna
lard
dryly
the
instances
gradual
gradually
dual
inimically
off
dullard
grad
equipage
gladly
mauritania
drug
a
drag
pickering
yard
daddy
on
lallygag

'''

#outputs
'''
dryad
duly
lard
dryly
gradual
gradually
dual
dullard
grad
gladly
drug
drag
yard
daddy
'''
def isMatchingWord(word, hexagonLetters):
    # isMatchingWord recibe una palabra y las letras
    #  en disposicion hexadecimal, retorna un booleano
    #  si la palabra es coincidente con hexagonLetters
    for letter in word:
        if letter not in hexagonLetters:
            return False
    return True


hexagonLetters = input()  
# entrada de las letras en disposicion hexadecimal     
mandatoryFirstHexagonletter = hexagonLetters[0] 
# Primera letra hexagonal obligatoria

numberOfDictionaryWords = int(input())  
# número de palabras del diccionario

for _ in range(numberOfDictionaryWords):
    dictionaryWord = input()
    # ingresa palabras del diccionario 
    if len(dictionaryWord) < 4: 
        # si la longitud es menor a 4
        continue                                            

    if mandatoryFirstHexagonletter not in dictionaryWord:
        # si la primera letra hexagonal obligatoria no 
        # esta en el diccionario de palabras
        continue

    if isMatchingWord(dictionaryWord, hexagonLetters):
        # Si es concidente
        print(dictionaryWord)