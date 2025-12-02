def multiplicar(*numeros):
    multiplicacion = 1
    for numero in numeros:
        multiplicacion *= numero
    return multiplicacion

def multiplicando_suma(multiplicador, *numeros):
    acumulador = 0
    for numero in numeros:
        acumulador += numero
    return acumulador * multiplicador

def contar_argumentos(*argumentos):
    contador = 0
    for argumento in argumentos:
        contador +=1
    return contador
