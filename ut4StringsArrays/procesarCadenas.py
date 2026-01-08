def procesar_cadena(cadena):
    return cadena.upper(), cadena.lower(), len(cadena)

cadena = "Gato"
tupla_cadena = procesar_cadena(cadena)
print(tupla_cadena)