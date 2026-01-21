def comprobar_cadenas(cadena):
    if cadena == "":
        raise ValueError("Debe rellenar todos los campos")



def comprobar_edad(edad):
    if edad < 0 or edad > 100:
        raise ValueError("El edad debe estar entre 0 y 100")
def comprobar_telefono(telefono):
    if telefono == "":
        raise ValueError("Debe rellenar todos los campos")
    elif len(str(telefono)) != 9:
        raise ValueError("El teléfono de tener 9 digitos")



persona = {
    "nombre":"",
    "edad" : 0,
    "dirección": "",
    "tlf": 0
}

bucleNombre = True
while bucleNombre:
    try:
        nombre = input("Por favor, introduzca su nombre").strip().title()
        comprobar_cadenas(nombre)
        persona["nombre"] = nombre
        bucleNombre = False
    except ValueError as e:
        print(e)

bucle_edad = True
while bucle_edad:
    try:
        edad = int(input("Por favor, introduzca su edad"))
        comprobar_edad(edad)
        persona["edad"] = edad
        bucle_edad = False
    except ValueError as e:
        print(e)

bucle_direccion = True
while bucle_direccion:
    try:
        direccion = input("Por favor, introduzca su direccion").strip().title()
        comprobar_cadenas(direccion)
        persona["dirección"] = direccion
        bucle_direccion = False
    except ValueError as e:
        print(e)

bucle_telefono = True
while bucle_telefono:
    try:
        tlf = int(input("Por favor, introduzca su telefono"))
        comprobar_cadenas(tlf)
        persona["tlf"] = tlf
        bucle_telefono = False
    except ValueError as e:
        print(e)
        print("Debes introducir solo números, sin letras ni símbolos")

print(f"{persona["nombre"]} tiene {persona["edad"]} años,"
      f" vive en {persona["dirección"]} y su número de telefóno es {persona["tlf"]}")