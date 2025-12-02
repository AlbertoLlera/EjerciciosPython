def saludar(nombre_funcion, saludo = "Hola"):
    return f"{saludo}, {nombre_funcion}"

nombre = input("Por favor, introduzca su nombre: ")
mensaje = saludar(nombre_funcion = nombre)
print(mensaje)