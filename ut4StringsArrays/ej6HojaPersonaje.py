personaje = {
    "nombre" : "",
    "edad" : "",
    "sexo": "",
    "tlf": "",
    "email" : "",
}

def info_diccionario():
    for key, value in personaje.items():
        print(f"{key}: {value}")



personaje["nombre"] = input("Por favor, indique le nombre del personaje")
info_diccionario()
personaje["edad"] = input("Por favor, indique la edad del personaje")
info_diccionario()
personaje["sexo"] = input("Por favor, indique la sexo del personaje")
info_diccionario()
personaje["tlf"] = input("Por favor, indique la tlf")
info_diccionario()
personaje["email"] = input("Por favor, indique la email")
info_diccionario()