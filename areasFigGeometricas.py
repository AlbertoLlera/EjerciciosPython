import moduleAreas as a

#Modulo calculos con tres funciones, una area circulo, area cuadrado, area cuadrado.
#Si alguno de los valores necesarios no se introduce, el valor recibido va a ser 8.

def opciones_menu():
    print("Por favor, pulse 1 para calcular el área de un cuadrado.\n"
          "Por favor, pulse 2 para calcular el área de un triángulo.\n"
          "Por favor, pulse 3 para calcular el área de un cuadrado.\n"
          "Por favor, pulse 4 para cerrar la aplicación.")

def validar_numero(numero):
    if numero < 0:
        raise ValueError("El numero no puede ser negativo")

menu = True
while menu:
    opciones_menu()
    num = None
    bucleNum = True
    while bucleNum:
        try:
            num = int(input("Ingresa un numero: "))
            validar_numero(num)
            bucleNum = False
        except ValueError as e:
            print(e)

    match num:
        case 1:
            lado = input("Introduzca la longitud del cuadrado: ")
            lado = 8 if lado == "" else float(lado)
            resultado = a.area_cuadrado(lado)
            print(f"El área del cuadrado es: {resultado}")
        case 2:
            base = float(input("Introduzca la longitud de la base: "))
            base = 8 if base == "" else float(base)
            altura = float(input("Introduzca la altura de la base: "))
            altura = 8 if altura == "" else float(altura)
            resultado = a.area_triangulo(base, altura)
            print(f"El área de su triángulo es: {resultado}")
        case 3:
            radio = float(input("Introduzca el radio del círculo: "))
            radio = 8 if radio == "" else float(radio)
            resultado = a.area_circulo(radio)
            print(f"El área del círculo es: {resultado}")
        case 4:
            menu = False
        case _:
            print("Número ingresado no valido")

