def analizar_numeros(numeros):
    pares = 0
    impares = 0
    total = 0

    for numero in numeros:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

        total += 1

    return total, pares, impares

lista_numeros = [34, 12, 7, 45, 23, 18, 39, 2, 51, 27, 14, 41, 9, 33, 19]

tupla_numeros = analizar_numeros(lista_numeros)

print(tupla_numeros)