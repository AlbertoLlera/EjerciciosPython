def empiezan_vocal(palabra):
    vocales = "aeiouáéíóú"
    return palabra[0].lower() in vocales

def acaban_consonante(palabra):
    vocales = "aeiouáéíóú"
    ultima_letra = palabra[-1]
    return ultima_letra.lower() not in vocales

def palabras_con_numeros(palabra):
    for i in range(len(palabra)):
        if palabra[i].isnumeric():
            return True
    return False


diccionario = {
    "vocal": [],
    "consonante": [],
    "numeros": []
}

texto = input("Por favor, ingrese su texto")
palabras_separadas = texto.split()


for palabra in palabras_separadas:
    if empiezan_vocal(palabra):
        diccionario["vocal"].append(palabra)

    if acaban_consonante(palabra):
        diccionario["consonante"].append(palabra)

    if palabras_con_numeros(palabra):
        diccionario["numeros"].append(palabra)

for clave, valor in diccionario.items():
    print(f"{clave}: {valor}")
