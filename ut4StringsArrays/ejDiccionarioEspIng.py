diccionario_espannol_ingles = {}

print("De introducir las palabras de la siguiente manera: "
      "español:inglés seguido. Cada connjunto debe estar separado por una coma")

conjunto_palabras = input("Por favor, ahora introduzca los conjuntos de palabras: ")

for conjunto in conjunto_palabras.split(","):
    print(f"{conjunto}")
    clave, valor = conjunto.split(":")
    diccionario_espannol_ingles[clave] = valor




frase_espannol = input("Por favor, introduzca una frase en español: ").strip().split()
for palabra in frase_espannol:
    if palabra in diccionario_espannol_ingles:
        print(diccionario_espannol_ingles[palabra], end=" ")
    else:
        print(palabra, end=" ")
