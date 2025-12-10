import random

from colorama import Fore, Back, Style, init
init()


def comprobarNumero(mensaje):
    validar_numero = False
    while not validar_numero:
        try:
            numero = int(input(mensaje))
            validar_numero = True
            return numero
        except ValueError:
            print(f"{Fore.RED}Debe ingresar un número, las cadenas de caracteres no están permitidas{Style.RESET_ALL}")



jugar_partida = True
while jugar_partida:
    intentos=0
    num_adivinar = random.randint(1,100)
    num_adivinado =False
    while not num_adivinado:
        num_jugador = comprobarNumero("Por favor, introduzca un número")
        if num_jugador < num_adivinar:
            print(f"{Fore.CYAN}El número que intentas adivinar es mayor{Style.RESET_ALL}")
        elif num_jugador > num_adivinar:
            print(f"{Fore.MAGENTA}El número que intentas adivinar es menor{Style.RESET_ALL}")
        else:
            num_adivinado = True
        intentos += 1
    print(f"{Fore.LIGHTYELLOW_EX}!Felicidades número adivinado¡ Te ha costado: {intentos} intentos{Style.RESET_ALL}")
    jugar_otra_vez = input("¿Quiére jugar de nuevo?Si-No")
    jugar_otra_vez_minus = jugar_otra_vez.lower()
    if jugar_otra_vez == "no":
        jugar_partida = False

print(f"{Fore.YELLOW}Fin del programa")
