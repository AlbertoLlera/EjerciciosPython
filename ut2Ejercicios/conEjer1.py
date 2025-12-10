numPos = False
while (numPos == False):
    try:
        edad = int(input("Introduzca su edad: "))#Esto no esta mal pero habría que crear una excepción propia. Esto se haría con el Except ValueError
        if edad > 0:
            numPos = True
        else:
            print("Los número introducidos deben ser positivos, nunca negativos")
    except:
        print("De introducir un valor")
if (edad >=18):
    print("Es mayor de edad")
else:
    print("No es mayor de edad")