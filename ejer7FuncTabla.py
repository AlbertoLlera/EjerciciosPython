def tabla_multiplicar(num, hasta = 10):
    tabla = []
    for i in range(1, hasta + 1):
        tabla.append(i * num)

    return tabla

numero = int(input("Introduce un numero: "))
tabla_de_multiplicar = tabla_multiplicar(numero)
for num in tabla_de_multiplicar:
    print(num)