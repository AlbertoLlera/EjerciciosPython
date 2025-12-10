numCorrecto = True

while numCorrecto:
    try:
        num = int(input("Por favor, introduzca un número entero:"))
        numCorrecto = False
    except:
        print("Debe introducir un número entero")

if (num % 2 == 0):
    print("El número ", num, "es par")
else:
    print("El número ", num, "es impar")