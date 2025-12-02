'''
Hacer una función que calcule el precio de una entrada precio_entrada().
Necesita conocer el precio de la entrada, que por defecto va a ser diez, la edad del asistente y si es o no estudiante
en caso de ser menor de 18 o estudiante tendrá un descuento del 50% de la entrada. Los descuentos no son acumulables
'''

def validar_numeros(num):
    if num < 0:
        raise ValueError("No se pueden introducir números negativos.")

def validar_cadenas(cadena):
    if cadena == "":
        raise ValueError("El campo no puede quedar vacio, debe introducir una cadena.")

def validar_estudiante(tipoEstudiante):
    if tipoEstudiante.lower() != "si" and tipoEstudiante.lower() != "no":
        raise ValueError("Por favor, indique si es o no estudiante.")

def precio_entrada(edadAsistente, estudiante, entrada = 10.0):
    if edadAsistente < 18 or estudiante:
        descuento = (50 * entrada) / 100
        return entrada - descuento
    return entrada


precio = None
bucle_entrada = True
while bucle_entrada:
    try:
        precio = float(input("Ingresa un precio de entrada: "))
        validar_numeros(precio)
        bucle_entrada = False
    except ValueError as e:
        print(e)

edad = None
bucle_edad = True
while bucle_edad:
    try:
        edad = float(input("Ingresa la edad: "))
        validar_numeros(edad)
        bucle_edad = False
    except ValueError as e:
        print(e)

siNo = ""
estudiante = None
bucle_estudiante = True
while bucle_estudiante:
    try:
        siNo = input("Indique con si es tudiante (introduzca si o no por teclado)")
        validar_cadenas(siNo)
        validar_estudiante(siNo)
        if siNo.lower() == "si":
            estudiante = True
            bucle_estudiante = False
        else:
            estudiante = False
            bucle_estudiante = False
    except ValueError as e:
        print(e)

precioDefinitivo = precio_entrada(edad, estudiante, precio)
input(f"El precio de la entrada es de {precioDefinitivo} euros")