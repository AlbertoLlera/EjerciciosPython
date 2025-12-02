def calcular_precio(precio_base, iva = 21):
    return precio_base * (1 + iva / 100)

precio_producto = float(input("Por favor, introduzca el valor del producto: "))
precio_pagar = calcular_precio(precio_producto)
print(f"El precio final de producto es de: {round(precio_pagar, 2)}")