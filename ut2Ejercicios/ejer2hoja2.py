
def comprobar_numero(numero):
    if numero < 0:
        raise ValueError("El número debe ser positivo")
    return numero

def comprobar_divisa(divisa):
    if divisa not in ["GBP", "USD", "JPY"]:#Esto es una lista, es decir, un list de Java para los amigos. También hay set, tuplas, etc.
        raise ValueError("El programa no soporta la divisa indicada")
    return divisa

def operacion_cambio(divisa, numero):
    cambio = 0
    match divisa:
        #RECORDAR: los float en python se ponen con puntos, con comas entiende que es una tupla
        case "GBP":
            cambio = numero * 0.87
        case "USD":
            cambio = numero * 1.08
        case "JPY":
            cambio = numero * 158.27
    return cambio

numPositivo= False

while not numPositivo:
    try:
        numero = float(input("Por favor, introduzca la cantidad de dinero que quiere convertir"))
        comprobar_numero(numero)
        numPositivo = True
    except ValueError as e:
        print(e)

divisaCorrecta = False

while not divisaCorrecta:
    try:
        divisa =input("Por favor, ahora introduzca la divisa")
        comprobar_divisa(divisa)
        divisaCorrecta = True
    except ValueError as e:
        print(e)

cambio = operacion_cambio(divisa, numero)
print(f"{numero} € son {cambio} {divisa}")
