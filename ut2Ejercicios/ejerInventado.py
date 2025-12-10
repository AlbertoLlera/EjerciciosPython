#Según una lista de números encuentra cuantos son positivos, negativos y cuantos 0 hay

numPositivos = 0
numNegativos = 0
cero = 0

for num in [10, -5, 0, -7, 46, 328, -54, 0, 78, -549] :
    if num < 0:
        numNegativos += 1
    elif num > 0 :
        numPositivos += 1
    else:
        cero += 1

print(f'El total de números negativos es de: {numNegativos}\nEl total de positivos es de: '
      f'{numPositivos}\nEl total de cero es de: {cero}')
