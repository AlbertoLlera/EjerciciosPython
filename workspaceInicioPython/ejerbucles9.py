
contador = 0
while True:
    if contador % 7 != 0:
        contador += 1
        continue
    elif contador % 7 == 0:
        if 80 < contador < 200:
            print(f"El primer multiplo de 7 mayor que 80, pero menor que 200 es: {contador}")
            break
    contador+=1
print("Fin del programa")

#Factorial de un número:
factorial = 1
num = int(input("Introduce un numero: "))
for i in range(1, num+1):
    factorial *= i
print(factorial)

#Suma digitos numero:
num = int(input("Introduce un numero: "))
suma_digitos = 0
while num > 0:
    ultimo_digito = int(num % 10)
    suma_digitos += ultimo_digito
    num /= 10

print(f"La suma de los digitos es de: {suma_digitos}")

termino = 1
while termino < 1000:
    termino *=2
    print(termino)

