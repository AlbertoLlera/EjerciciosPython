def analizar_texto(texto):
    palabras = texto.split()
    num_palabras = len(palabras)
    primera_palabra = palabras[0]

    return len(texto), num_palabras, primera_palabra

cadena_texto = "Feliz año nuevo"

tupla = analizar_texto(cadena_texto)

print(tupla)