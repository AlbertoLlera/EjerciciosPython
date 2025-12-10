
def comprobar_num(mensaje):
    validar_numero = False
    while not validar_numero:
        try:
            num = int(input(mensaje))
            validar_numero = True
            return num
        except ValueError:
            print("Cadenas no permitidad. Por favor, introduzca un número: ")
    return None


def comprobar_primo(numero):
    contador = 2


    while contador < numero:
        if numero % contador == 0:
            return False
        contador += 1

    return True

num = comprobar_num("Por favor, introduzca un número: ")

if num == 1:
    print(f"El número {num} es primo")
else:
    for i in range (2,num+1):
        if comprobar_primo(i):
            print(f"El número {i} es primo")
        else:
            print(f"El número {i} no es primo")