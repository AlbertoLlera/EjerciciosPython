def comprobar_numero (numero):
    if numero < 0:
        raise ValueError("El número no puede ser negativo")
    return numero

def es_primo (numero):
    #no_es_primo = False

    if numero < 2:
        #no_es_primo = True
        return False
    else:
        for i in range(2, numero):
            if numero % i == 0:
                #print(f"El número {num} no es primo")
                #no_es_primo = True
                return False

    return True

validar_numero = False
num = None
while not validar_numero:
    try:
        num = int(input("Por favor, introduzca un número: "))
        comprobar_numero(num)
        validar_numero = True
    except ValueError as e:
        print(e)

if es_primo(num):
    print(f"El número {num} es primo")
else:
    print(f"El número {num} no es primo")