'''
numTelefono = input("Ingrese el número de teléfono: ")
numTroceado = numTelefono.split("-")
print(numTroceado[1])
'''

'''
numLoteria = []

cantidadNumeros = int(input("Cuantos números desea almacenar: "))
for i in range(cantidadNumeros):
    num = int(input(f"Por favor, introduzca el nñumero {i+1}"))
    numLoteria.append(num)
'''
'''
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(numeros), 0, -1):
    print(i, end=", ")
'''

asignaturas = ["Python", "Servidor", "Cliente", "Interfaces", "IPII"]

for i in range(len(asignaturas)):
    nota = int(input(f"Calificación obtenida en {asignaturas[i]}: "))
    if nota < 5:
        asignaturas.remove(asignaturas[i])

print(asignaturas)


