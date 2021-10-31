##Ejercicio 5 continuacion de la clase pasada  
# el siguiente codigo define una funcion que recibe una lista y va eliminando de mitada en mitad
# si la lista queda con un solo elemento entonces retorna ese mismo
#
# Complejidad: Se presencia el recorrido del bucle deisminuyendose a la mitad
# en cada iteracion por lo evidenciado en clase la complejidad resultante es de
# Por lo que el resultado seria la multiplicacion de estos
# O(log(n))
# 
# Entrada:
# -
# Salida:
# El valor resultante de la eliminacion 
# 
# Autor:  Yeimy Huanca

def pick_resume(resumes):
    eliminate = "top"
    while len(resumes) > 1:          
        if eliminate == "top":          
          resumes = resumes[(len(resumes)//2): len(resumes)] 
          eliminate = "bottom"      
        elif eliminate == "bottom":
          resumes = resumes[0: len(resumes)//2]
          eliminate = "top"          
    return resumes

resumes = [5,3,79,14,2,55,13,15,17,6,24,56]
print("Sobreviviente", pick_resume(resumes))

resumes = [1,15,17,6,24,56]
print("Sobreviviente", pick_resume(resumes))