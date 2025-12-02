#Ejecución
import operaciones as op

#Llamadas a funciones del ejercicio
total_argumentos = op.info_argumentos(4,5,6,7,8,9,12,45,76,23)
print(f"El total de argumentos es: {total_argumentos}")

op.divisibles3(4,5,6,7,8,9,12,45,76,23)

op.histograma(4, 9, 7)

#Llamada a la función del ejercicio2
#Pruebo a darle un kilo y una tarifa de envio ya fijada previamente, pero no es urgente aún. El resultado es 12
coste_envio1 = op.coste_envio(1, 10)
print(f"Coste del envio 1: {coste_envio1}")

#Prueba 2. Le damos 5 kilos, no indicamos el precio del envio, por tanto se le aplica la tarifa base de 5 euros y envio urgente para añdirle un sobre coste del 30%
coste_envio2 = op.coste_envio(5, urgente=True)
print(f"Coste del envio 2: {coste_envio2}")

#Prueba3. Indicamos kilos, tarifa de envio y que el mismo es urgente
coste_envio3 = op.coste_envio(3, tarifa_envio=8, urgente=True)
print(f"Coste del envio 3: {coste_envio3}")

#Prueba4. En este caso solo indicamos los kilos del paquete
coste_envio4 = op.coste_envio(9)
print(f"Coste del envio 4: {coste_envio4}")

#Prueba5. Llamamos a la función, esta vez le indicamos todos los datos, solo que dejamos el envio urgente en false
coste_envio5 = op.coste_envio(12, 20, urgente=False)
print(f"Coste del envio 5: {coste_envio5}")

coste_envio6 = op.coste_envio(0, 20, urgente=False)
print(f"Coste del envio 5: {coste_envio6}")




#Ejercicio3
horas = 0
minutos = 0
segundos = 0

bucle_horas = True
while bucle_horas:
    try:
        horas = int(input("Por favor, ingrese la hora (respete el formato 24h): "))
        op.validar_hora(horas)
        bucle_horas = False
    except ValueError as e:
        print(e)

bucle_minutos = True
while bucle_minutos:
    try:
        minutos = int(input("Por favor, ingrese los minutos (respete el formato 0-60): "))
        op.validar_minutos_segundos(minutos)
        bucle_minutos = False
    except ValueError as e:
        print(e)


bucle_segundos = True
while bucle_segundos:
    try:
        segundos = int(input("Por favor, ingrese los segundos (respete el formato 0-60): "))
        op.validar_minutos_segundos(segundos)
        bucle_segundos = False
    except ValueError as e:
        print(e)

#Llamada a la función ejercicio3
resultado = op.convertir_segundos(horas, minutos, segundos)
print(f"Total de segundos: {resultado}")