def comprobar_cadena(cadena):
    if cadena == "":
        raise ValueError("La cadena no puede estar vacia")

divisas = {
    "Euro" : "€",
    "Dolar" : "$",
    "Yen" : "¥"
}

bucle = True
respuesta_usuario = ""
while bucle:
    try:
        respuesta_usuario = input("Por favor, que divisa quiere comprobar: ").strip().title()
        comprobar_cadena(respuesta_usuario)
        bucle = False
    except ValueError as e:
        print(e)

claves_diccionario = divisas.keys()

if respuesta_usuario in claves_diccionario:
    clave = divisas.get(respuesta_usuario)
    print(f"El símbolo del {respuesta_usuario} es: {clave}")
else:
    print(f"{respuesta_usuario} no esta en el diccionario")
