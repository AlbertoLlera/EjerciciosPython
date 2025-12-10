intentos = 1

while True:
    contrasenia = input("Por favor, introduzca su contraseña (tiene tres intentos)")
    if contrasenia == "python123":
        print("Contraseña correcta")
        break
    elif intentos >=3:
        print("Ha superado todos los intentos, cuenta bloqueada")
        break
    intentos +=1