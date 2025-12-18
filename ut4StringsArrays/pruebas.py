#Esta prueba lo que hace es ordenadar alfabeticamente teniendo en cuenta el código ASCII [a-zA-Z]
#Iría antes hello que world si buscasemos de menor a mayor
cadena = "Hello"
cadena2 = "world"

orden_alfabetico = ""
if cadena > cadena2:
    orden_alfabetico = cadena
else:
    orden_alfabetico = cadena2

print(f"La cadena que aprece después alfabéticamente es: {orden_alfabetico}")
#Hola Raquel



letras = ["a", "b", "c", "d", "e"]

for letra in letras[::-1]:
    print(letra)
