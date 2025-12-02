def formatear_nombre(nombre, apellido, orden="nombre_apellido"):
    if orden == "apellido_nombre":
        nombre_completo = f"{apellido} {nombre}"
    else:
        nombre_completo = f"{nombre} {apellido}"
    return nombre_completo

nom = input("Por favor, introduzca el nombre: ")
ape = input("Por favor, introduzca el apellido: ")
num_orden = int(input("Introduzca 1 para (nombre_apellido) o 2 para (apellido-nombre): "))

if num_orden == 1:
    print(f"Hola, {formatear_nombre(apellido = ape, nombre = nom)}")
else:
    print(f"Hola, {formatear_nombre(nombre = nom, apellido = ape, orden = "apellido_nombre")}")