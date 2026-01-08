'''Dos funciones, saludo despedida. Tupla con saludar y despedir, si concide con alguno de los elementos se llama a la función saludar'''

def saludar():
    print("Hola, bienvenido a 2026")

def despedir():
    print("Hasta luego, cara huevo")

tupla = ("saludar", "despedir")

recogidaTeclado = input("Indique si quiere saludar o despedir: ")

recogidaTeclado = recogidaTeclado.lower()


if recogidaTeclado in tupla:
    match recogidaTeclado:
        case "saludar":
                saludar()
        case "despedir":
                despedir()
else:
    print("No ha introducido ni despedir ni saludar, error")