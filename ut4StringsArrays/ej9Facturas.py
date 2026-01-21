facturas = {}

cantidades = {
    "Pagos" : 0,
    "Pendientes" : 0
}

def annadir_factura():
    identificador_factura = int(input("Introduzca el numero de factura"))
    if identificador_factura in facturas:
        print("El numero de factura ya existe")
        return
    else:
        cantidad_factura = float(input("Introduzca la suma de la factura a pagar"))
        facturas[identificador_factura] = cantidad_factura
        cantidades["Pendientes"] += 1
        return

def pagar_factura():
    identificador_pago = int(input("Introduzca el numero de pago"))
    if identificador_pago not in facturas:
        print("El numero de identificación de factura no existe")
        return
    else:
        cantidades["Pagos"] += facturas[identificador_pago]
        cantidades["Pendientes"] -= 1
        facturas.pop(identificador_pago)
        return

def resumen():
    for key, value in cantidades.items():
        print(f"{key} -> {value}")


bucle_menu = True
while bucle_menu:
    print("Introduzca 1 si desea añadir facturas")
    print("Introduzca 2 si desea pagar una factura")
    print("Introduzca 3 si desea finalizar")
    num_menu = int(input("Introduzca la opción que deseas consultar"))

    match num_menu:
        case 1:
            annadir_factura()
            resumen()
        case 2:
            pagar_factura()
            resumen()
        case 3:
            resumen()
            print("Gracias por confiar en pagos facturas S.L.")
            bucle_menu = False