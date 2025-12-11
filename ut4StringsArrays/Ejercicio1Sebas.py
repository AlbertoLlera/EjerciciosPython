cadena = "               este ejercicio es muy complicado            "

#.strip() basicamente quita los espacios al principio y al final. Es como .trim()
cadena_sin_espacios_inicio_fin = cadena.strip()
print(f"La cadena sin espacios: {cadena_sin_espacios_inicio_fin}")

#Modicafos una de las palabras de la cadena con replace
cadena_modificada = cadena_sin_espacios_inicio_fin.replace("complicado", "facil")
print(f"{cadena_modificada}")

#Convierto la primera letra de cada una de las palabras a mayus con .title()
cadena_mayus = cadena_modificada.title()
print(cadena_mayus)

#Eliminamos todos los espacios de la cadena. Usamos nuevamente .replace()
cadena_sin_ningun_espacio = cadena_mayus.replace(" ", "")
print(cadena_sin_ningun_espacio)

#Invertimos la cadena
cadena_invertida = cadena_mayus[::-1]
print(cadena_invertida)

#Buscamos el indice de la palabra complicado con .find()
indice_complicado = cadena_sin_espacios_inicio_fin.find("complicado")
print(indice_complicado)
