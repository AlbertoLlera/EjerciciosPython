'''
¿Qué hace la función?
Recibe una cadena y un reemplazo, que por defecto es un asterisco, pero que podría ser cualquier otra cosa.
En el return usamos .join() que va a ir uniendo caracter a caracter. El "" del principio es para que lo junte sin espacios.
Luego establecemos el condicional que es la lógica.
Después creamos el bucle .enumerate() pilla indice y character, entonces en el for definimos i para el indice y
char para el caracter.
'''
def cambiar_por_asteriscos(cadena, reemplazo="*"):
    return "".join(
        reemplazo if i % 2 == 0 else char
        for i, char in enumerate(cadena)
    )

cadena = input("Introduce una cadena de caracteres, por favor: ")

cadena_sin_espacios = cadena.replace(" ", "").lower()
print(cadena_sin_espacios)

cadena_asteriscos = cambiar_por_asteriscos(cadena_sin_espacios)
print(cadena_asteriscos)

'''
cadena_con_asteriscos = ""
for i in range(0, len(cadena_sin_espacios), 1):
    if i % 2 == 0:
        cadena_con_asteriscos += "*"
    else:
        cadena_con_asteriscos += cadena_sin_espacios[i]

print(cadena_con_asteriscos)
'''
