def comprobar_mayus(cadena):
    return cadena.isupper()

cad = input("Por favor, introduzca una cadena de caracteres: ")
if comprobar_mayus(cad):
    print("Todos los caracteres estan en mayuscula")
else:
    print("No esta todos los caracteres en mayuscula")