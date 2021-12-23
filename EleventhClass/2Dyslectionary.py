def sort(longest, words):
    for w in sorted(words, key = lambda w: w[::-1]):
        padding = ' ' * (longest - len(w))
        print(f'{padding}{w}')

longest, words = -1, []
# Longest> Longitud de la palabra mas larga , Words >Bloque de palabras a ordenar desde atras

while True:
    #lectura
    try:
        word = input()
        if not word:
            sort(longest, words)
            # Ordena el bloque desde atras
            print()
            longest, words = -1, []
            # Reinicia las variables
        else:
            longest = max(longest, len(word))
            # Recalcular longitud maxima de las palabras
            words.append(word)
            # Agregar nuestra palabra al bloque actual

    # En caso de error ,break
    except EOFError:
        sort(longest, words)
        # Ordena e imprimimos ultimo bloque ingresado
        break
        # Rompe el ciclo para recibir datos o input
        
        