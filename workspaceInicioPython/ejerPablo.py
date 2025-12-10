def cadena_numero(numero):

    try:
        numero = int(numero)
    except ValueError:
        print("El número no puede ser una cadena de caracteres")

    return numero

def numero_negativo(numero):
    if numero < 0:
        raise ValueError("Numero debe ser positivo")

    return numero

def introducir_numero():
    num = None
    validar_numero = False
    while not validar_numero:
        try:
            num = input("Por favor, introduzca un número:")
            num = cadena_numero(num)
            if type(num) == int:  # No vale con if num is int, hay que usar la función tipe para que realmente compruebe que num es del tipo int
                num = numero_negativo(num)
                validar_numero = True
        except ValueError as e:
            print(e)
    return num

def elegir_plato():
    print("Pulse 1 para elegir hamburguesa con patatas")
    print("Pulse 2 para elegir sandwich mixto")
    print("Pulse 3 para elegir con ensalada campera")
    print("Pulse cualquier otro número si no desea añadir un plato principal")

    num = introducir_numero()

    match num:
        case 1:
            return "Hamburguesa con patatas"
        case 2:
            return "Sandwich mixto"
        case 3:
            return "Ensalada campera"
        case _:
            return "Sin plato principal"

def elegir_bebida():
    print("Pulse 1 para elegir agua")
    print("Pulse 2 para elegir coca-cola")
    print("Pulse 3 para elegir té helado de melocotón")
    print("Pulse cualquier otro número en caso de no querer bebida")

    num = introducir_numero()

    match num:
        case 1:
            return "Agua"
        case 2:
            return "Coca-cola"
        case 3:
            return "Té helado de melocotón"
        case _:
            return "Sin bebida"

def elegir_complemento():
    print("Pulse 1 para elegir alitas de pollo")
    print("Pulse 2 para elegir tequeños")
    print("Pulse 3 para elegir gyozas de verduras")
    print("Pulse cualquier otro número si no desea añadir un complemento")

    num = introducir_numero()

    match num:
        case 1:
            return "Alitas de pollo"
        case 2:
            return "Tequeños"
        case 3:
            return "Gyozas de verduras"
        case _:
            return "Sin complemento"

def main():
    menu = []
    menu.append(elegir_plato())#append()es una función que basicamente te ayuda a introducir elementos al final de una lista
    menu.append(elegir_bebida())
    menu.append(elegir_complemento())
    #menu = [elegir_plato(), elegir_complemento(), elegir_bebida()] versión resumida indicada por el id de lo que había hecho yo al inicio
    print("Productos del pedido:")
    for plato in menu:
        print(plato)

main()