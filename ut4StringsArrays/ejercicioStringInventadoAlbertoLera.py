'''
El ejercicio consiste en lo siguiente:
Se debe validar un mail introducido por consola por el usuario,
se debe comprobar que el mail contenga
Para ello habrá que usar una función que devuelva true o false,
además el usuario solo tendrá tres oportunidades para introducir el mail.
'''

def validar_email(email):
    email_valido = False
    if '@' in email and (email.endswith('.com') or email.endswith('.es')):
        return True

    return False


cont = 0
while cont < 3:
    correo = input(f"Por favor, introduzca el email. Tiene tres intentos, intento número {cont + 1}: ")
    if validar_email(correo):
        print(f"El correo {correo} es valido")
        break
    else:
        print(f"El correo {correo} introducido no es valido, revise que tiene @ y caba en .com o .es)")
        cont+=1

    if cont == 3:
        print(f"Ha superado el número de intentos permitidos")

print("Gracias por confirmar su email")
