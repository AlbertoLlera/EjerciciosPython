#Función ganador, devuelve un ganador entre varios que yo le pase, el nombre que devuelva tiene que ser aleatorio.
from random import randrange
def ganador (*participantes):
    #contador = 0
    num_participantes = len(participantes) + 1
    '''
    for participante in participantes:
        contador += 1
    '''
    aleatorio = randrange(num_participantes)
    return participantes[aleatorio]

winner = ganador("Sebas", "Alberto", "Monica", "Franco", "Alda", "Ana", "Manu", "Carlos", "Malpelo", "Pacheco", "Pablo", "Rafa", "Bermejo")
print(f"El ganador es: {winner}")

