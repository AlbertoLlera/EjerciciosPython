def mostrar_info(nombre, edad, ciudad="Madrid"):
    return f"Hola {nombre}, persona de {edad} eres de {ciudad}"

def crear_usuario(nombre, email, estado=True):
    if estado:
        return f"Bienvenido usuario {email} (Nombre: {nombre} estás conectado)"
    else:
        return f"El usuario {email}, no está conectado"

print(mostrar_info(nombre = "Ataulfo", edad = 78))

print(crear_usuario(nombre = "Hadrian Marlow", email = "melodramatico@gmail.com", estado = False))
print(crear_usuario( email= "niño_de_papa@gmail.com", nombre = "Crispin Marlow"))
