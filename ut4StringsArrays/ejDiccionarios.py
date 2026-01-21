#Si algún alumno tiene menos de 5, se actualiza a 5 como tal

nestesDicctionary= {
    "est1" : {
        "nombre" : "Alberto",
        "nota" : 8
    },
    "est2" : {
        "nombre" : "Sebas",
        "nota" : 6
    },
    "est3" : {
        "nombre" : "Mónica",
        "nota" : 4
    }
}

for estudiante, datos in nestesDicctionary.items():
    for clave, valor in datos.items():
        #No funcionaba, porque intetaba comparar una cadena con un int
        if clave == "nota":
            if valor < 5:
                datos[clave] = 5
                print(f"Nota de {datos['nombre']} actualizada, ahora tiene un 5")
            else:
                print(f"Nota de {datos['nombre']} es: {valor}")