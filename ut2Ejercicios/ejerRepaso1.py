'''
cont = 1
suma_numeros = 0

while cont < 100:
    suma_numeros += cont
    cont += 1

print(suma_numeros)
'''
'''
num = int(input("Ingresa un numero: "))
comprobar_primo = False
if num == 1:
    print("El numero es no primo")
else:
    for i in range(2, num):
        if num % i == 0:
            comprobar_primo = True
            break
    if not comprobar_primo:
        print("El numero es primo")
    else:
        print("No es primo")
'''
'''
def validar_numero(mensaje):
    no_es_cadena = False

    while not no_es_cadena:
        try:
            numero = int(input(mensaje))
            no_es_cadena = True
            return numero
        except ValueError:
            print("Debe introducir números, no cadenas de caracteres")

def calcular_celsius(farenheit):
    celsius =  5/9 * (farenheit - 32)
    return celsius

def calcular_farenheit(celsius):
    farenheit = 9/5 * (celsius + 32)
    return farenheit

print("Pulse 1 para calcular conversion celsius a farenheit")
print("Pulse 2 para calcular conversion  farenheit celsius")

num_menu = validar_numero("Ingresa un numero: ")

match num_menu:
    case 1:
        grados_farenheit = validar_numero("Ingresa la temperatura de grados farenheit:")
        celsius = calcular_celsius(grados_farenheit)
        print(f"Estamos a {celsius} grados celsius")
    case 2:
        grados_celsius = validar_numero("Ingresa la temperatura de grados celsius:")
        farenheit = calcular_farenheit(grados_celsius)
        print(f"Estamos a {farenheit} grados farenheit")
    case _:
        print("Opción no valida")
'''
'''
numero_fibonacci = int(input("Ingresa un numero: "))

num_anterior = 0
num_actual = 1

for i in range(1, numero_fibonacci + 1):
    siguiente = num_actual + num_anterior
    num_anterior = num_actual
    num_actual = siguiente
    if i != numero_fibonacci:
        print(num_actual, end=', ')
    else:
        print(num_actual)
'''
'''
def calcular_impuesto(sueldo_bruto):
    if sueldo_bruto <= 10000:
        return sueldo_bruto
    elif 10001 <= sueldo_bruto <= 30000:
        return sueldo_bruto * 0.10
    else:
        return sueldo_bruto * 0.20

sueldo = int(input("Por favor, ingrese su sueldo: "))
impuestos = calcular_impuesto(sueldo)

if sueldo == impuestos:
    print("Usted cobra menos de 10000 €, no paga impuestos")
else:
    print(f"Con su sueldo de {sueldo}€ deberá pagar: {impuestos} de impuestos")
'''
'''
bucle = False
cont = 0

while not bucle:
    if cont > 10:
        bucle = True
    else:
        print(f"Estamos en la iteración del bucle número {cont}")
    cont += 1
print("Fin del programa")
'''


def numeros_amigos(numero):

    cont = 0
    for i in range(1, numero):
      if numero % i == 0:
          cont += i
    return cont


num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa un numero: "))

sum_divisores_num1 = numeros_amigos(num1)
sum_divisores_num2= numeros_amigos(num2)

if num1 == sum_divisores_num2 and num2 == sum_divisores_num1:
    print(f"El numero {num1} es amigo del {num2}")
else:
    print(f"El numero {num1} no es amigo del {num2}")