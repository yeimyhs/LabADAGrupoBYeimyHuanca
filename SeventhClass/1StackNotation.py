##Ejercicio 1
# el siguiente codigo usa la estructura ya implementada para identificar elementos y simbolos
# matematicos para realizar su respectivaoperacion
#  
# Stack -ref https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks
#
# Entrada:
#                     Casos de prueba planteados  
# Salida:
# 
# Input: 2 1 + 3 *
# Output: 9
#or
# Input: 4 13 5 / +
# Output: 6
#or
# Input: 10 6 9 3 + -11 * / * 17 + 5 +
# Output: 12
#
# Autor:  Yeimy Huanca


#Casos de prueba descomentar para probar----
#  
#
input = "2 1 + 3 *" 
#input = "4 13 5 / +" 
#input = "10 6 9 3 + -11 * / * 17 + 5 +"
#-------------------------------------------
data= input.split(" ")
mathsimb= "+-*/"
stack = []
for i in data:
    if (i in mathsimb):
            b = stack.pop()
            a = stack.pop()
            if (i == "+"):
                stack.append(a+b)
            elif (i == "-"):
                stack.append(a-b)
            elif (i == "*"):
                stack.append(a*b)
            else:
                stack.append(a//b)
    else:
            stack.append(int(i))
            continue
print('Input:',input)
print('Output:',stack[0])
