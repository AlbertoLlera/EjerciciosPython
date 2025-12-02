def comprobar_primo(numero):
    if numero == 1:
        return False
    if numero == 2:
        return True

    for i in range (2,numero):
        if numero % i == 0:
            return False

    return True

num = int(input("Ingresa un numero: "))
if comprobar_primo(num):
    print(f"El numero {num} es primo")
else:
    print(f"El numero {num} no es primo")