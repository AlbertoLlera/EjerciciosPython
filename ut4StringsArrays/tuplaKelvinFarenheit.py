def convertir_temperatura(celsius):
    farenheit = 9 / 5 * celsius + 32
    kelvin = celsius - 32

    return farenheit, kelvin

celsius = 2

tupla =convertir_temperatura(celsius)

print(tupla)