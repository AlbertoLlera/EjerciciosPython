def diccionario_cadena(cadena):
    diccionario = {
        "longitud" : len(cadena),
        "minus": cadena.lower(),
        "ultimas5Letras": cadena[-5:]
    }

    return diccionario

cad = input("Por favor, introduzca una cadena:")

datosFuncion = diccionario_cadena(cad)

for clave, valor in datosFuncion.items():
    print(F"{clave}: {valor}")

