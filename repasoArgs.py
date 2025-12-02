def primera_ultima_letra(*palabras):
    '''
    total_palabras = len(palabras)
    primera_palabra = palabras[0]
    ultima_palabra = palabras[total_palabras-1]
    totalLetrasUltima = len(ultima_palabra)
    '''

    return palabras[0][0] + palabras[-1][-1]

print(primera_ultima_letra("hola", "pavo", "gato", "vaca", "arconte", "bebé"))
