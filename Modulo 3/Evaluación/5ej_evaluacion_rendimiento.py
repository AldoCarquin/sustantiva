import math

materias = ['Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Música', 'Arte']
lenguaje = [3, 4, 5, 6]
matematicas = [5, 6, 3, 5]
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


def ver(asignatura, materias):
    print(f'\n*** LAS NOTAS SON LAS SIGUIENTES ***')

    for m in materias:
        match m:
            case 'Lenguaje':
                asignatura = list(lenguaje)
            case 'Matemáticas':
                asignatura = list(matematicas)
            case 'Historia':
                asignatura = list(historia)
            case 'Ciencias':
                asignatura = list(ciencias)
            case 'Música':
                asignatura = list(musica)
            case 'Arte':
                asignatura = list(arte)
            
        prom = promedio(asignatura)
        print(f'\n{m}: Promedio {prom}')
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

def main(materias, asignatura):

    menu = int(input('Opción:'))
    while menu != 4:
        match menu:
            case 1:
                ver(asignatura, materias)
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
    main(materias, asignatura)



