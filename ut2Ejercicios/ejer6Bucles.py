
def aprobados(notas_lista):
    aprobados = []
    for i in lista_notas:
        if i >= 5:
            aprobados.append(i)

    return len(aprobados)

lista_notas = [8, 5, 10, 8.32, 3.25, 7, 2.25, 4.5, 6]

total_notas = 0
nota_media = 0
nota_mas_alta = lista_notas[0]
nota_mas_baja = lista_notas[0]
num_aprobados = 0

for nota in lista_notas:

    if nota > nota_mas_alta:
        nota_mas_alta = nota
    elif nota < nota_mas_baja:
        nota_mas_baja = nota
    total_notas += 1
    nota_media += nota


num_aprobados = aprobados(lista_notas)
print(f"El número de aprobados es de: {num_aprobados}")
print(f"La nota más alta del curso es: {nota_mas_alta}")
print(f"La nota más baja del curso es: {nota_mas_baja}")
print(f"La nota media del curso es: {nota_media/total_notas}")