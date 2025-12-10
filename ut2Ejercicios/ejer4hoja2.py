def comprobar_numero(numero):
    if numero < 0:
        raise ValueError("El número debe ser positivo")
    return numero

saldo = None
numSaldo = False
while not numSaldo:
    try:
        saldo = float(input("Por favor, introduzca su saldo"))
        comprobar_numero(saldo)
        numSaldo = True
    except ValueError as e:
        print(e)

retirada = None
numRetirada = False
while not numRetirada:
    try:
        retirada = float(input("Por favor, introduzca la cantidad de dinero que quiere retirar"))
        comprobar_numero(retirada)
        numRetirada = True
    except ValueError as e:
        print(e)

if saldo < retirada:
    print("No dispone de saldo suficiente")
else:
    saldo -= retirada
    print(f"Saldo retirado correctamente. Su saldo actual es de: {saldo}")