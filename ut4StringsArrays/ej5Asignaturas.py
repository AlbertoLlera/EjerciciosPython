asignaturas = {
    'Matemáticas' : 6,
    'Física' : 4,
    'Química' : 5
}

totalCreditos = 0

for key, value in asignaturas.items():
    totalCreditos += value
    print(f"{key} tiene {value} creditos")

print(f"El total de créditos del curso es de: {totalCreditos}")