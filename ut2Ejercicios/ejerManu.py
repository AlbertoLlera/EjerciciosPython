#Bucles, estructuras de control y control de errores. Inventario de manzanas, platanos y peras, que te permita alñadir x numeros, venderlas, mostrar lo que tienes en el inventario y salid
#Un menú para una fruteria que lleve la cuenta de manzanas, peras y platanos. Mostrar, vender, comprar y salir

#Metodo para comprobar que se meten números y no cadenas
def comprobar_numero(mensaje):
    num = 0
    validar_numero = True
    while validar_numero:
        try:
            num = int(input(mensaje))
            validar_numero = False
        except ValueError:
            print("El valor introducido debe ser un número, no una cadena de carácteres")
    return num

#Metodo para completar una venta de frutas
def vender_frutas(cantidad_frutas, vendidas):

        if vendidas > cantidad_frutas:
            raise ValueError("No dispone de frutas suficientes para completar la venta")

        return cantidad_frutas - vendidas

#Metodo para una compra de frutas
def comprar_frutas(cantidad_frutas, compradas):
    cantidad_frutas += compradas
    return cantidad_frutas

#Menú para seleccionar el tipo de frutas
def menu_frutas ():
    fruta_seleccionada = None

    print("Pulse 1 para vender manzanas")
    print("Pulse 2 para para vender platanos")
    print("Pulse 3 para vender peras")

    num_menu_frutas = comprobar_numero("Por favor, introduzca el número de la fruta que desea vender")

    match num_menu_frutas:
        case 1:
            fruta_seleccionada = "Manzanas"
        case 2:
            fruta_seleccionada = "Platanos"
        case 3:
            fruta_seleccionada = "Peras"
        case _:
            print("La opción seleccionada no existe")

    return fruta_seleccionada


manzanas = 10
platanos = 10
peras = 10

menu = True
while menu:
    print("Pulse 1 para comprobar inventario")
    print("Pulse 2 para vender frutas")
    print("Pulse 3 para comprar frutas")
    print("Pulse 4 para salir de la aplicación")

    num_menu = comprobar_numero("Introduzca el número de la opción que desea realizar:")

    match num_menu:
        case 1:
            print(f"Total manzanas: {manzanas}\nTotal platanos: {platanos}\nTotal peras: {peras}")
        case 2:
            fruta_seleccionada = menu_frutas()
            vendidas = comprobar_numero("Por favor, indique la cantidad que quiere vender")
            try:
                if fruta_seleccionada == "Manzanas":
                    manzanas = vender_frutas(manzanas, vendidas)
                    print(f"Venta exitosa, tras la venta quedan: {manzanas}")
                elif fruta_seleccionada == "Platanos":
                    platanos = vender_frutas(platanos, vendidas)
                    print(f"Venta exitosa, tras la venta quedan: {platanos}")
                else:
                    peras = vender_frutas(peras, vendidas)
                    print(f"Venta exitosa, tras la venta quedan: {peras}")
            except ValueError as e:
                print(e)
        case 3:
            fruta_seleccionada = menu_frutas()
            compradas = comprobar_numero("Por favor, indique la cantidad que quiere comprar")
            if fruta_seleccionada == "Manzanas":
                manzanas = comprar_frutas(manzanas, compradas)
                print(f"Compra exitosa, ahora tenemos: {manzanas}")
            elif fruta_seleccionada == "Platanos":
                platanos = comprar_frutas(platanos, compradas)
                print(f"Compra exitosa, ahora tenemos: {platanos}")
            else:
                peras = comprar_frutas(peras, compradas)
                print(f"Compra exitosa, ahora tenemos: {peras}")
        case 4:
            print("Gracias por confiar en Frutillas S.L.")
            menu = False
        case _:
            print("La opción seleccionada no existe")




