import random


def advinar_posicion(num_aleatorio, tupla):
    return tupla.index(num_aleatorio)

tupla_numeros = (8, 4, 1, 9, 3, 6, 10, 2, 5, 7)

num_aleatorio = random.randint(1,10)
print(f"El número aleatorio: {num_aleatorio}, está en la posición "
      f"{advinar_posicion(num_aleatorio, tupla_numeros) + 1} de la tupla")