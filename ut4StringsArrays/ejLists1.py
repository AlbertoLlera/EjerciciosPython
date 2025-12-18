#Funciones ejercicios
def nueva_lista_nombres (lista_nombres1):
    lista_nombres2 = []

    for nombre in lista_nombres1:
        if len(nombre) == 4:
            lista_nombres2.append(nombre)
    return lista_nombres2

def reemplazar_menores(annios):
    for i in range (len(annios)):
        if annios[i] < 18:
            annios[i] = "Menor"
    return annios

def evitar_duplicados(numeros):
    for numero in numeros:
        if numero in numeros:
            numeros.remove(numero)
    return numeros

def rotar_lista(letras):
    lista_rotada = []
    for letra in letras[::-1]:
        lista_rotada.append(letra)
    return lista_rotada

def primer_ultimo(lista_numeros):
    primer_elemento = lista_numeros[0]
    ultimo_elemento = lista_numeros[-1]
    lista_numeros[0] = ultimo_elemento
    lista_numeros[-1] = primer_elemento
    return lista_numeros

def lista_slicing(numeros):
    lista_pares = numeros[::2]
    return lista_pares


'''
Dada la lista nombres = ["Ana", "Juan", "Luis", "Eva", "Mario"],
usa list comprehension para crear una nueva lista que contenga solo nombres de 4 letras.
'''

nombres = ["Ana", "Juan", "Luis", "Eva", "Mario"]
nombres_cuatro_letras = nueva_lista_nombres(nombres)
print(nombres_cuatro_letras)

'''
Dada la lista:
edades = [12, 18, 25, 15, 30, 17]
Reemplaza todas las edades menores de 18 por el valor "Menor".
'''

edades = [12, 18, 25, 15, 30, 17]

edades = reemplazar_menores(edades)
print(edades)


'''
Dada la lista:
valores = [1, 2, 2, 3, 4, 4, 5, 1]
Crea una nueva lista sin elementos duplicados, manteniendo el orden original.
'''
valores = [1, 2, 2, 3, 4, 4, 5, 1]
valores_sin_duplicados = evitar_duplicados(valores)
valores_sin_duplicados.sort()
print(valores_sin_duplicados)

'''
Dada la lista:
letras = ["a", "b", "c", "d", "e"]
Rota la lista una posición a la derecha.
'''

letras = ["a", "b", "c", "d", "e"]
letras_rotadas = rotar_lista(letras)
print(letras_rotadas)

'''
Dada una lista cualquiera, intercambia el primer y el último elemento.
[10, 20, 30, 40]
'''

lista_ejemplo = [10, 20, 30, 40]
print(primer_ultimo(lista_ejemplo))

'''
Dada la lista:
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Crea una nueva lista con los números pares usando slicing.
'''

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
solo_pares = lista_slicing(numeros)
print(solo_pares)

'''
Dada la lista:
datos = [10, "hola", 5.5, "adiós", 3, "Python"]
Crea dos listas:
una con los números
otra con las cadenas de texto
'''

datos = [10, "hola", 5.5, "adiós", 3, "Python"]
lista_cadenas = []
lista_numeros = []

for dato in datos:
    if isinstance(dato, str):
        lista_cadenas.append(dato)
    else:
        lista_numeros.append(dato)

print("Lista con las cadenas:")
print(lista_cadenas)
print("Lista con los números:")
print(lista_numeros)