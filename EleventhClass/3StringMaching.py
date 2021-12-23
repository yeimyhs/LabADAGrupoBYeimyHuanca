import sys

def construct_partial_match_table(pattern):   
    string_length = len(pattern)            
    current_prefix_length = 0                                       

    partial_match_table = [0] * string_length

    if string_length == 1:
        return partial_match_table

    # Repite cada carácter del patrón para comprobar los sufijos parciales en diferentes puntos del patrón.
    # Comienza en el índice 1 porque en el índice 0, si no, no habria un sufijo  posible
    for current_index, current_char in enumerate(pattern[1:], 1):
        # Si se tuviera un sufijo parcial que coincidiera con un prefijo adecuado, 
        # pero el siguiente carácter de la cadena rompe la coincidencia, la
        # longitud de coincidencia parcial máxima posible es el valor de la tabla 
        # en el índice anterior (coincidencia más reciente) Reitera esto hasta 
        # que carácter al que ahora apuntamos coincide con el carácter actual (o la 
        # longitud del prefijo es 0, lo que significa que no hay coincidencia parcial en este índice)
        while current_prefix_length > 0 and pattern[current_prefix_length] != current_char:
            current_prefix_length = partial_match_table[current_prefix_length - 1]

        if pattern[current_prefix_length] == current_char:
            current_prefix_length += 1
        partial_match_table[current_index] = current_prefix_length
    return partial_match_table


# algoritmo Knuth-Morris-Pratt (coincidencia de cadenas)
def kmp_string_search(given_string, pattern):
    # tabla de coincidencias 
    table = construct_partial_match_table(pattern)
    given_string_length = len(given_string)
    pattern_length = len(pattern)

    index_to_begin_search = 0
    given_index = 0
    pattern_index = 0
    locations_of_matches = []

    # Itera a través de cada carácter de la cadena que deseamos comprobar.
    while given_string_length - index_to_begin_search > pattern_length:
        # Si bien el carácter actual en nuestra subcadena y la cadena dada coinciden, incremente cada
        # uno en 1 para comparar los siguientes caracteres (a menos que llegue al final de la cadena)
        while pattern_index < pattern_length and given_string[given_index] == pattern[pattern_index]:
            given_index += 1
            pattern_index += 1
        if pattern_index >= pattern_length:
            locations_of_matches.append(str(index_to_begin_search))
        if pattern_index > 0 and table[pattern_index - 1] > 0:
            index_to_begin_search = given_index - table[pattern_index - 1]
            pattern_index = table[pattern_index - 1]

        # Si esta coincidencia está al principio de la cadena y no ha encontrado ningún carácter en nuestra subcadena en
        # el actual index_to_begin_search, incrementa given_index en 1 para comenzar a buscar allí.
        # actualizamos index_to_begin_search y  pattern_index (si aún no está al comienzo de nuestra subcadena)
       
        else:
            if given_index == index_to_begin_search:
                given_index += 1
            index_to_begin_search = given_index
            if pattern_index > 0:
                pattern_index = table[pattern_index - 1]

    if given_string[-pattern_length:] == pattern:
        locations_of_matches.append(str(len(given_string) - pattern_length))
    print(' '.join(locations_of_matches))

# CASO DE PRUEBA
# Inicialice todas las variables booleanas y de cadena que usaremos durante nuestra prueba
string_to_check = ''
pattern_to_check = ''
check_ready = False

# Leer cada línea independientemente del stdin
# En las líneas impares, se nos da el patrón para verificar
# En las líneas pares, se nos da la cadena para verificar
for line in sys.stdin:
    if not check_ready:
        pattern_to_check = line.rstrip('\n')
        check_ready = True
    else:
        string_to_check = line.rstrip('\n')
        check_ready = False
        kmp_string_search(string_to_check, pattern_to_check)