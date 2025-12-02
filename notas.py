def calificacion(nota):
    resultado = ''
    match nota:
        case 0 | 1 | 2 | 3 | 4:
            resultado = 'Suspenso'
        case 5:
            resultado = 'Suficiente'
        case 6:
            resultado = 'Bien'
        case 7 | 8:
            resultado = 'Notable'
        case 9 | 10:
            resultado = 'Sobresaliente'
        case _:
            resultado = 'Nota introducida incorrecta'

    return resultado


notaObtenida = int(input('Por favor, ingrese la nota que ha obtenido en este examen: '))
print(f'Ha obtenido en el último examen un: {calificacion(notaObtenida)}')