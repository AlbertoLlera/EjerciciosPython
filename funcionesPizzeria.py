def make_pizza(comensales, *ingredientes):
    print(f"Pizza para {comensales} comensales con los siguientes ingredientes:")
    for ingrediente in ingredientes:
        print (ingrediente, end=",")

    print(ingredientes)


totalComensales =  int(input("Ingrese el número de comensales: "))
make_pizza(totalComensales, "queso", "tomate", "peperoni", "beicon", "carne picada")

#Función ganador, devuelve un ganador entre varios que yo le pase, el nombre que devuelva tiene que ser aleatorio.
#Modulo calculos con tres funciones, una area circulo, area cuadrado, area cuadrado. Si alguno de los valores necesarios no se introduce, el valor recibido va a ser 8.