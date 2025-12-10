menuFuncionando = True

while menuFuncionando:
    print("Introduzca 1 para ver perfil")
    print("Introduzca 2 para editar perfil")
    print("Introduzca 3 para salir")
    numMenu = int(input("Por favor, introduzca un número:"))


    match numMenu:
        case 1:
            print("Mostrando perfil")
        case 2:
            print("Modificando perfil...")
        case 3:
            print("Saliendo...")
            menuFuncionando = False

print("Fin de programa")