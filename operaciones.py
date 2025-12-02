#Funciones ejercicio1
def info_argumentos(*numeros):
    contador = 0
    for numero in numeros:
        print(numero)
        contador += 1
    return contador

def divisibles3(*numeros):
    for numero in numeros:
        if numero % 3 == 0:
            print(f"{numero} es divisible 3")

def histograma(*numeros):
    for numero in numeros:
        asterisco = ''
        for i in range(0, numero):
            asterisco += '*'
        print(asterisco)

#Funciones ejercicio2
def coste_envio(kilos, tarifa_envio = 5, urgente = False):
    coste = None
    if kilos >= 1:
        coste = tarifa_envio + (kilos * 2)
    else:
        coste = tarifa_envio

    if urgente:
        aumento_recargo = coste * 0.30
        coste += aumento_recargo
    return coste


#Funciones ejercicio3
def validar_hora(hora):
    if hora < 0 or hora > 24:
        raise ValueError('La variable horas debe respetar el formato de 24 (No pueden ser menores de 0 o mayores de 24)')

def validar_minutos_segundos(numero):
    if numero < 0 or numero > 60:
        raise ValueError('Debe respetar minutos/segundos (No pueden ser menores de 0, ni mayores que 60)')

def convertir_segundos(horas, minutos, segundos):
    horas_segundos = horas * 3600
    minutos_segundos = minutos * 60
    return horas_segundos + minutos_segundos + segundos