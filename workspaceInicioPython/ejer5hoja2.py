#Que vaya recogiendo numeros hasta que introduzca uno negativo

num = 0

while num >= 0:
    num = int(input("Por favor, introduzca un número (Si quiere salir, introduzca un número negativo)"))
    if num == 0 or num < 0:
        continue
    else:
        print(num)
print("Se acabó")