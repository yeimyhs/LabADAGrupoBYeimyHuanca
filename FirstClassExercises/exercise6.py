##Ejercicio 6
# el siguiente codigo modifica el programa anterior 
# para definir el número de espacios entre el marco y las palabras.
# Entrada: 3
#  Hello World!
# Salida:
# ********************
# *                  *
# *                  *
# *                  *
# *   Hello World!   *
# *                  *
# *                  *
# *                  *
# ********************
#
# Autor:  Yeimy Huanca
print("ejercicio6")
word = input("word:")
simb='*'
marco ='*'
relleno = '*'
num= int(input("number:"))
#marco=(simb*len(word))+(num*simb)+(simb*2)
for j in range(len(word)+((num)*2)):
  marco+='*'
marco+=simb
for i in range(len(word)+((num)*2)):
  relleno+=' '
relleno+=simb
relleno+=('\n'+relleno)*(num-1)
word = simb+(' '*num)+word+(' '*num)+simb

print (marco)
print (relleno)
print (word)
print (relleno)
print (marco)