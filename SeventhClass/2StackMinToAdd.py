##Ejercicio 2
# el siguiente codigousa stacks para hallar el numero de parentesis
# a agregar para que el la expresion sea logica(unicamente parentesis)  
#  
# Stack -ref https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks
#
# Entrada:
#                     Casos de prueba planteados  
# Salida:
# 
# process: ---------------------------
# stack: ['(']
# stack: ['(', '(']
# stack: ['(', '(', '(']
# Result: ---------------------------
# Input: (((
# Output: 3
#
# Autor:  Yeimy Huanca


#Casos de prueba descomentar para probar----
#  
#
input = "())" 
#input = "(((" 
#input = "(()))(" 
#input = "()))(("

#-------------------------------------------
stack = [] 
print("process: ---------------------------")
for i in input:
    if(i in "("): 
        stack.append(i)
        print("stack:",stack)
    elif(i in ")"):
        if(len(stack) == 0 or stack[-1] in ")"):
            stack.append(i)
            print("stack:",stack)
        elif(stack[-1] in "("):
            stack.pop()
            print("stack:",stack)
print("Result: ---------------------------")
print('Input:',input)
print('Output:',len(stack))
