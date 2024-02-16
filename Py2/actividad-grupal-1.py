numero = int(input("ingrese número:"))

rango = []

cantidad = 100 - numero

print(f"El numero ingresado es {numero}")

if numero % 2 == 0:
    print(f"El numero {numero} es par")
    for i in range(cantidad, 0, -2):
        rango.append(100 - i + 2)

else:
    print(f"El numero {numero} es impar")
    for i in range(cantidad, 0, -2):
        rango.append(99 - i + 1)

print(f"resultado: {rango}")



