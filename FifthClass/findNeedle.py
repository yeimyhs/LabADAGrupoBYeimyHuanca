##Ejercicio 1   de N^2 a N
# el siguiente codigo busca un string dado dentro de otro string brindado
# si encuentra la coincidencia imprime True de lo contrario false
#
# Complejidad: Se presencia dos bucles , uno recorre la cantidad de el primer string N 
# y el segundo recorre la cantidad del otro M
# Por lo que el resultado seria la multiplicacion de estos
# O(n*m)
# 
# Entrada:
# -
# Salida:
# False
# True
# 
# Autor:  Yeimy Huanca

def findNeedle(needle, haystack):
    ndl_i = 0
    hstk_i = 0
    encontrado = False
    while hstk_i < len(haystack):
        if needle[ndl_i] == haystack[hstk_i]:
            encontrado = True
            while ndl_i < len(needle):
                if needle[ndl_i] != haystack[hstk_i + ndl_i]:
                    encontrado = False
                    break
                ndl_i += 1

            if encontrado:
                return True
            ndl_i = 0

        hstk_i += 1
    return False

string1 = "abcdefghi"
string2 = "gfhi"
string3 = "cde"

print(findNeedle(string2, string1))#false
print(findNeedle(string3, string1))#true