def num_mas_grande(*numeros):
    num_mayor = 0
    for numero in numeros:
        if numero > num_mayor:
            num_mayor = numero
    return num_mayor

def contar_digitos(numero):
    contador = 0
    while numero > 0:
        contador += 1
        numero = numero // 10

    return contador

def sumar_digitos(numero):
    digitos_sumados = 0
    while numero > 0:
        ultimo_digito = numero % 10
        digitos_sumados += ultimo_digito
        numero = numero // 10
    return digitos_sumados

def cambiar_orden_numero(numero):
    num_reves = 0
    while numero > 0:
        digito = numero % 10
        num_reves = num_reves * 10 + digito
        numero = numero // 10
    return num_reves

def suma_mayores_que(limite, *numeros):
    suma_mayores = 0
    for numero in numeros:
        if numero > limite:
            suma_mayores += numero
    return suma_mayores

print(f"El número más grande es: {num_mas_grande(10, 7, 8)}")
print(f"El número 5947493024749 tiene: {contar_digitos(5947493024749)} digitos")
print(f"La suma del número 23 es: {sumar_digitos(23)}")
print(f"El número 567 al revés es: {cambiar_orden_numero(567)}")

print(f"la suma de los numeros mayores en la secuencia es de {suma_mayores_que(30,59, 47, 493, 82, 474, 9)}")