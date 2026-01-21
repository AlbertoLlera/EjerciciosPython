cad = "Hola, el objetivo de este ejercicio es contar vocales"

vocales = {
    "a" : 0,
    "e" : 0,
    "i" : 0,
    "o" : 0,
    "u" : 0
}

for i in range(0, len(cad)):
    if cad[i] in vocales:
        vocales[cad[i]] += 1

print(vocales)