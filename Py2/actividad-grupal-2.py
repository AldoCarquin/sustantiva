notas = []

for i in range(5):
    while True:
        try: 
            nota = float(input(f"Ingrese la nota {i + 1}: "))

            if 0 <= nota <= 10:
                notas.append(nota)
                break
            else:
                print("Nota no válida. Por favor ingrese una nota entre 0 y 10.")
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")

suma_notas = sum(notas)
leng_notas = len(notas)
promedio = suma_notas/leng_notas
ordenadas = sorted(notas)

print(f"Las notas son: {notas}")
print(f"La media aritmeética es {promedio}.")
print(f"La media posicional es {ordenadas[2]}.")
print(f"La nota menor es {ordenadas[0]}.")
print(f"La nota mayor es {ordenadas[4]}.")