def calculoHoras(horas, ratio):
    if horas > 40:
        horasExtra = horas - 40
        salarioExtra = ratio * 1.5 * horasExtra
        pago = (40 * ratio) + salarioExtra
    else:
        pago = horas * ratio + 5 * 15
        print('Salario mensual: ', pago)

    return pago

horas = float(input('Ingresa horas: '))
ratio = float(input('Ingresa salario: '))

print(f"El sueldo final es de: {calculoHoras(horas, ratio)}")

