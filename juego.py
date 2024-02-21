import random

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
diaEscogido = 0
print(f"Los días de la semana son los siguientes:")
for dia in dias:
    print(f"- {dia}")
print("Estos días están ordenados en una lista.\nPor ende vamos a aprender cómo utilizar la posición de índice de estos días según sea el caso.\n*******************\nA continuación, aleatoriamente se asignará un día.\nUsted debe ser capaz de identificar su índice.\nConsiderando que los índices comienzan desde el 0.")

while True:
    try:
        dialeatorio = random.choice(dias)
        print(f"El día seleccionado es {dialeatorio}.")
        diaEscogido = int(input(f"Seleccione el índice al que corresponda el día {dialeatorio}:"))
        indiceCorrecto = dias.index(dialeatorio)
        
        if diaEscogido == indiceCorrecto:
            print(f"¡Correcto! El índice es el que corresponde.")
            break
        else:
            print("Incorrecto.")
    except ValueError:
        print("Ingrese un número válido.")
        
    break

        