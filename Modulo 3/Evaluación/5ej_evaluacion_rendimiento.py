import math

lenguaje = [3, 4, 5, 6]
matematica = [5, 6, 3, 5]
historia = [2]
ciencias = [2, 2, 2]
musica = [4, 5, 2]
arte = []

asignatura = []

def hayNota(asignatura):
    if len(asignatura) == 0:
        print(f'La asignatura no tiene notas.\n')
    else:
        for i in range(len(asignatura)):
            if i < len(asignatura) - 1:
                print(asignatura[i], end=',')
            else:
                print(asignatura[i], end='\n')


def ver(lenguaje, matematica, historia, ciencias, musica, arte, asignatura):
    print(f'\n*** LAS NOTAS SON LAS SIGUIENTES ***')
    
    # LENGUAJE
    asignatura = list(lenguaje)
    prom = promedio(asignatura)
    print(f'LENGUAJE: Promedio {prom}')
    hayNota(asignatura)

    asignatura = list(matematica)
    prom = promedio(asignatura)
    print(f'\n\nMATEMÁTICAS: Promedio {prom}')
    hayNota(asignatura)

    asignatura = list(historia)
    prom = promedio(asignatura)
    print('\n\nHISTORIA: Promedio {prom}')
    hayNota(asignatura)

    asignatura = list(ciencias)
    prom = promedio(asignatura)
    print('\n\nCIENCIAS: Promedio {prom}')
    hayNota(asignatura)

    asignatura = list(musica)
    prom = promedio(asignatura)
    print(f'\n\nMÚSICA: Promedio {prom}')
    hayNota(asignatura)

    asignatura = list(arte)
    prom = promedio(asignatura)
    print(f'\n\nARTE: Promedio {prom}')
    hayNota(asignatura)


def promedio(asignatura):
    if len(asignatura) == 0:
        promedio = None
    else:
        promedio = sum(asignatura)/len(asignatura)
    return promedio

print('****** BIENVENIDE AL EVALUADER ******\n')
print('*** POR FAVOR  INGRESE UNA OPCIÓN ***')
print('1.- Ver notas.')
print('2.- Agregar nota.')
print('3.- Borrar nota.')
print('4.- Salir')

def main(lenguaje, matematica, historia, ciencias, musica, arte, asignatura):

    menu = int(input('Opción:'))
    while menu != 4:
        match menu:
            case 1:
                ver(lenguaje, matematica, historia, ciencias, musica, arte, asignatura)
            case 2:
                print('Opcion 2')
            case 3:
                print('Opcion 3')
            case 4:
                print('*** SALIENDE DEL EVALUADER ***')
            case _:
                print('MENU NO VALIDO!!!\nINGRESE MENU DEL 1 AL 4')
        menu = int(input('Opción:'))
    

if __name__ == "__main__":
    main(lenguaje, matematica, historia, ciencias, musica, arte, asignatura)



