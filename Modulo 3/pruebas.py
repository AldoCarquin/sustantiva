lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8]

for i in range(len(lista_numeros)):
    if i < len(lista_numeros) - 1:
        print(lista_numeros[i], end=',')
    else:
        print(lista_numeros[i], end='')

# Salida: 1,2,3,4,5,6,7,8