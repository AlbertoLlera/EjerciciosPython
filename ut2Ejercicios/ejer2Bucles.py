from colorama import Fore, Back, Style, init
init()

def comprobar_numero(mensaje):
    validar_numero = False
    while not validar_numero:
        try:
            numero = int(input(mensaje))
            validar_numero = True
            return numero
        except ValueError:
            print(f"{Fore.RED}Debe ingresar un número, las cadenas de caracteres no están permitidas{Style.RESET_ALL}")
    return None

multiplicar = lambda numero1, numero2: numero1 * numero2

def tabla_multiplicar(numero):
    '''
    for i in range(1, 11):
        print(f"{Fore.MAGENTA}{i} * {numMultiplicar} = {multiplicar(i, numero)}{Style.RESET_ALL}")
    else:
        print(f"{Fore.LIGHTCYAN_EX}Fin del programa")
    '''

    resultados = []

    for i in range (1, 11):
        resultados.append(multiplicar(i, numero))

    return resultados


numMultiplicar = comprobar_numero("Por favor, introduzca un número: ")
tablaMultiplicar = tabla_multiplicar(numMultiplicar)
print(f"Resultados de la tabla de multiplcar del {numMultiplicar}: {tablaMultiplicar}")