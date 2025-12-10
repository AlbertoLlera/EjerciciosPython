numCorrecto = False

while numCorrecto == False:
    try:
        nota = float(input("Introduzca su nota"))
        if nota >= 0 and nota <= 10:
            numCorrecto = True
        else:
            print("Debe introducir un valor entre 0 y 10, ambos incluidos")
    except:
        print("Por favor, debe introducir números")


notaSinDecimales = int(nota)

match notaSinDecimales:
    case 0|1|2|3|4:
        print("Suspenso")
    case 5|6:
        print("Aprobado")
    case 7|8:
        print("Notable")
    case 9|10:
        print("Sobresaliente")
    case _:#Default de Java
        print("Sobresaliente")
