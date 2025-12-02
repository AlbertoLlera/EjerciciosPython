def my_function(multiplicador, *numeros):
    total = 0

    for numero in numeros:
        multiplicar = numero * multiplicador
        print(f"{numero} x {multiplicador} = {multiplicar}")
        total += multiplicar

    return total


suma = my_function(5,1, 2, 3, 34, 67, 123456, 90476392, 45532)
print(f"Resultado de la suma: {suma}")