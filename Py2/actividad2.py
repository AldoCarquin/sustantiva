cantidad = int(input("Ingrese cantidad de notas: "))

contador = 0

notas = []

for i in range(cantidad):
    nota = float(input(f"Ingrese la nota {i + 1}: "))
    notas.append(nota)


suma_notas = sum(notas)
leng_notas = len(notas)
promedio = suma_notas/leng_notas

for dato in  notas:
    if dato > promedio:
        contador += 1

print(f"El promedio es {promedio} de un total de {leng_notas} totales.")
print(f"Existen {contador} notas mayores que el promedio.")
print(f"Las notas son: {notas}")