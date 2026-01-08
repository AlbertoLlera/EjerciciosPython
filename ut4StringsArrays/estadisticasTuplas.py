def calcular_estadisticas(numeros):
    estadisticas = []
    estadisticas.append(max(numeros))
    estadisticas.append(min(numeros))
    estadisticas.append(sum(numeros) / len(numeros))

    tupla = tuple(estadisticas)

    return tupla

listaNumeros = [5, 6543, 94930, 3, 5, 123456789, 769]

tupla_estadisticas = calcular_estadisticas(listaNumeros)
print(tupla_estadisticas)
