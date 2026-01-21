frutas = {
    "Platano" : 1.35,
    "Manzana" : 0.80,
    "Pera" : 0.85,
    "Naranaja" : 0.70
}

frutaTeclado = input("Introduzca el tipo de fruta que desea comprar: ").strip().title()
cantidad = float(input("Indique la cantidad: "))

precioFinal = 0

if frutaTeclado in frutas:
    precioFinal = frutas[frutaTeclado] * cantidad
    print(f"El precio final es: {round(precioFinal, 2)}")
else:
    print(f"Fruta no encontrada")