def cadena_numero(numero):

    try:
        numero = int(numero)
    except ValueError:
        print("El número no puede ser una cadena de caracteres")

    return numero

def numero_negativo(numero):
    if numero < 0:
        raise ValueError("Numero debe ser positivo")

    return numero

def calcular_dinero(inversion, interes, annios):
    interes_decimal = interes/100
    for annio in range(1, annios + 1):
        capital_final = inversion * (1 + interes_decimal) ** annio
        print(f"Año {annio}: {capital_final:}")

def funcion_inversion():
    validar_inversion = True
    while validar_inversion:
        try:
            inversion = input("Por favor, introduzca la inversión que desea realizar:")
            inversion = cadena_numero(inversion)
            if type(inversion) == int:
                inversion = numero_negativo(inversion)
                validar_inversion = False
        except ValueError as e:
            print(e)
    return inversion


def funcion_interes():
    validar_interes = True
    while validar_interes:
        try:
            interes = input("Por favor, introduszca el tipo de interes anual:")
            interes = cadena_numero(interes)
            if type(interes) == int:
                interes = numero_negativo(interes)
                validar_interes = False
        except ValueError as e:
            print(e)

    return interes

def funcion_annios():
    validar_annios = True
    while validar_annios:
        try:
            annios = input("Por favor, introduzca el número de años:")
            annios = cadena_numero(annios)
            if type(annios) == int:
                annios = numero_negativo(annios)
                validar_annios = False
        except ValueError as e:
            print(e)
    return annios


inversion = funcion_inversion()
interes = funcion_interes()
annios = funcion_annios()
calcular_dinero(inversion, interes, annios)