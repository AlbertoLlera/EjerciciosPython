esNum = True

while esNum:
    try:
        edad = int(input("Por favor, introduzca su edad:"))
        esNum = False
    except:
        print("La edad debe ser un número entero")

if edad <= 13:
    print("Lamentablemente no puede conducir")
elif edad < 16:
    print("Puede conducir motos de poca cilindrada")
elif edad < 18:
    print("Puede conducir motos de alta cilindrada")
else:
    print("Puede conducir coches")