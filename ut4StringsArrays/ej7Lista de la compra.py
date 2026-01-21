lista_compra = {}

total_pagar = 0

while True:
    articulo_lista = input("Ingrese el artículo (Introduzca s o S si no desea introducir más artículos)")
    if articulo_lista[0] == "S" or articulo_lista[0] == "s":
        break

    precio_articulo = float(input("Ingrese el precio del artículo"))

    lista_compra[articulo_lista] = precio_articulo
    total_pagar += precio_articulo

for key, value in lista_compra.items():
    print(f"{key} -> {value}")

if len(lista_compra.keys()) != 0:
    print(f"Total de pagados: {total_pagar}")