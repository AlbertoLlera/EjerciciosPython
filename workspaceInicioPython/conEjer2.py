esNum = False
while (esNum == False):
    try:
        num1 = int(input("Introduzca el primer número"))
        num2 = int(input("Introduzca el segundo"))

        #if (type(num1) == int and type(num2) == int):
        esNum = True
    except:
        print("Los valores introducidos deben ser números")

if (num1 > num2):
    print(num1, " es mayor que ", num2)
elif (num1 == num2):
    print("Los dos números son iguales")
else:
    print(num2, " es mayor que ", num1)