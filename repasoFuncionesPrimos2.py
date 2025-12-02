def validar_primo(numero):
    if numero == 1:
        return False
    if numero == 2:
        return True

    for x in range(3, numero):
        if numero % x == 0:
            return False
    return True


num1 = 1
num2 = 25

for i in range(num1, num2):
    if validar_primo(i):
        print(f"El numero {i} es primo")