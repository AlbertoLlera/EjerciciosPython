def comprobar_numero (numero):
    if numero < 0:
        raise ValueError("El número no puede ser negativo")
    return numero

def es_primo (numero):
    noEsPrimo = False

    if num < 2:
        noEsPrimo = True
    else:
        for i in range(2, numero - 1):
            if numero % i == 0:
                print(f"El número {num} no es primo")
                noEsPrimo = True
                break

    if not noEsPrimo:
        print(f"El número {numero} es primo")

numPositivo = False
num = None
while not numPositivo:
    try:
        num = int(input("Por favor, introduzca un número"))
        comprobar_numero(num)
        numPositivo = True
    except ValueError as e:
        print(e)

es_primo(num)







