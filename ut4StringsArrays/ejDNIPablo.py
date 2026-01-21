def comprobar_dni(dni):
    letras_dni = "TRWAGMYFPDXBNJZSQVHLCKE"
    numeros_dni = int(dni[:-1])
    letra_dni = dni[-1]
    numero_letra = letras_dni.index(letra_dni)
    resultado_formula = numeros_dni % 23

    if resultado_formula == numero_letra:
        return True

    return False

dni = input("Por favor, introduzca su DNI").strip().upper()
if comprobar_dni(dni):
    print("DNI valido")
else:
    print("DNI invalido")
