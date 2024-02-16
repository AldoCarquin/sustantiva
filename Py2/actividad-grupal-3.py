meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
month = 0
while True:
    try:
        numero = int(input("Ingrese un número de mes del 1 al 12:")) - 1
        if 0 <= numero < len(meses):
            mes=meses[numero]
            print(f"El mes seleccionado es {mes}")

            if numero == 1:
                print(f"El mes de {mes} tiene 28 días. A no ser de que sea año bisiesto y serían 29 días.")
            elif numero == 0 or numero == 2 or numero == 4 or numero == 6 or numero == 7 or numero == 9 or numero == 11:
                print(f"El mes de {mes} tiene 31 días")
            else:
                print(f"El mes de {mes} tiene 30 días")
                
        else:
            print("El número ingresado no corresponde a un mes.")
        break
    except ValueError:
        print("Ingrese sólo un número del 1 al 12 por favor.")