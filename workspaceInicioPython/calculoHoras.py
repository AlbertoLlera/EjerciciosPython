try:
    horas = int(input("Introduzca las horas trabajadas: "))
    ratio = int(input("Introduzca el ratio de trabajo: "))
except:
    print('No puede introducir cadenas de texto')

if horas > 40:
    horasExtra = horas - 40
    salarioExtra = ratio * 1.5 * horasExtra
    pago = (40 * ratio) + salarioExtra
    print('Salario mensual: ', pago)
else:
    pago = horas * ratio + 5 * 15
    print('Salrio mensual: ', pago)