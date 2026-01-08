tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 1, 5, 7, 9, 6)

#Creas una tupla que almacena true o false en base si son pares o impares y luego en el count se comprueba el los que son true
impares = tuple(num % 2 !=0 for num in tupla)
total_impares = impares.count(True)

print(total_impares)