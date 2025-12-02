def filtar_pares(list_nums):
    num_pares = []
    for numeros in list_nums:
        if numeros % 2 == 0:
            num_pares.append(numeros)
    return num_pares

numeros = [4, 7, 12, 15, 22, 3, 8, 17, 24, 9, 10, 31, 6, 19, 28]
pares = filtar_pares(numeros)
for num in pares:
    print(num)