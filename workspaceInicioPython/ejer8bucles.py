def num_cadena(mensaje):
    try:
        numero = int(input(mensaje))
        return numero
    except ValueError:
        print("Debe introducir un número, no una cadena")


def validar_num(num):
    if num < 0:
        raise ValueError("El numero no puede ser negativo")



bucle_validaciones = False
while not bucle_validaciones:
    num = num_cadena("Por favor, introduzca un número")
    if type(num) == int:
        try:
            validar_num(num)
            bucle_validaciones = True
        except ValueError as e:
            print(e)

cuenta_atras=""
for i in range(num, -1, -1):
    if i != 0:
        print(i, end=", ")
    else:
        print(i)
    '''
    numero_convertido = str(i)
    if cuenta_atras:
        cuenta_atras = cuenta_atras +", " + numero_convertido
    else:
        cuenta_atras = cuenta_atras + numero_convertido
    '''
print(cuenta_atras)