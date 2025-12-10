from colorama import Fore, Back, Style, init#Esta línea importa la libreria de los colores
init()#Necesario en windows para que inicie

def comprobarNumero(mensaje, tipo):
    entradaValida = False
    while not entradaValida:
        try:
            numero = tipo(input(f"{Fore.CYAN}{mensaje}{Style.RESET_ALL}:"))
            entradaValida = True
            return numero
        except ValueError:
            print(f"{Fore.RED}Debe introducir números, "
                  f"las cadenas de carácteres no están permitidas{Style.RESET_ALL}")


sumar = lambda numero1, numero2: numero1 + numero2

restar = lambda numero1, numero2: numero1 - numero2

multiplicar = lambda numero1, numero2: numero1 * numero2

dividir = lambda numero1, numero2: numero1 / numero2


menuActivo = True

while menuActivo:
    print("Pulse 1 para sumar:")
    print("Pulse 2 para restar")
    print("Pulse 3 para multiplicar")
    print("Pulse 4 para dividir")
    print("Pulse 5 para salir de la calculadora")

    numMenu = comprobarNumero("Introduzca la opción del menú que desea realizar", int)


    if numMenu < 5:
        num1 = comprobarNumero("Introduzca el primer número que desea operar", float)
        num2 = comprobarNumero("Introduzca el segundo mensaje que desea operar", float)

    match numMenu:
        case 1:
            resultado = sumar(num1, num2)
            print(f"{Fore.LIGHTGREEN_EX}{num1} - {num2} = {resultado}{Style.RESET_ALL}")
        case 2:
            resultado = restar(num1, num2)
            print(f"{Fore.LIGHTGREEN_EX}{num1} - {num2} = {resultado}{Style.RESET_ALL}")
        case 3:
            resultado = multiplicar(num1, num2)
            print(f"{Fore.LIGHTGREEN_EX}{num1} * {num2} = {resultado}{Style.RESET_ALL}")
        case 4:
            divisor_valido = False
            while not divisor_valido:
                try:
                    num1 / num2
                    divisor_valido = True
                    resultado = dividir(num1, num2)
                    print(f"{Fore.LIGHTGREEN_EX}{num1} / {num2} = {resultado}{Style.RESET_ALL}")
                except ZeroDivisionError:
                    print(f"{Fore.RED}El divisor no puede ser 0{Style.RESET_ALL}")
                    num2 = float(input("Por favor, introduzca de nuevo el divisor"))
        case 5:
            menuActivo = False

print(f"{Fore.LIGHTMAGENTA_EX}Programa finalizado con exito.{Style.RESET_ALL}")






"""
Libreria para dar color a las salidas por pantalla en el terminal con ejemplos
from colorama import Fore, Back, Style, init

# Inicializar colorama (necesario en Windows)
init()

print(Fore.RED + 'Texto rojo')
print(Fore.GREEN + 'Texto verde')
print(Fore.BLUE + 'Texto azul')
print(Back.YELLOW + Fore.BLACK + 'Texto negro sobre amarillo')
print(Style.BRIGHT + 'Texto brillante')
print(Style.RESET_ALL)  # Resetear todos los estilos

# También puedes usar f-strings
print(f"{Fore.CYAN}Texto cyan {Style.BRIGHT}con brillo{Style.RESET_ALL}")
"""