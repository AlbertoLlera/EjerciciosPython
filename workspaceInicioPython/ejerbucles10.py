import random

termino = int(input("Ingresa un numero: "))

for i in range(1, termino + 1):
    if i % 2 != 0:
        print(i)
    else:
        print(f"{i * -1}")

suma = 0
num = None
while num != 0:
    num = int(input("Ingresa un numero(introduzca 0 para finalizar): "))
    suma += num
print(f"La suma de todos los números es: {suma}")

print("Pulse 1 para lanzar el dado")
print("Pulse 2 para detener el programa")
menu = True
while menu:

    num_menu = int(input("Ingresa un numero: "))

    match num_menu:
        case 1:
            print("Lanzas el dado...")
            print(f"Ha sacado un: {random.randint(1, 6)}")
        case 2:
            print("Gracias por lanzar el dado.")
            menu = False
        case _:
            print("La opción elegida no existe")