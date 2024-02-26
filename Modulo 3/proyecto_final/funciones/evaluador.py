import math

materias = ['Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Música', 'Arte']
lenguaje = []
matematicas = []
historia = []
ciencias = []
musica = []
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

def masNota():
    nota = int(input('Nota a agregar:'))
    while nota < 0 or nota > 7:
        nota = int(input('Valor no valido. Ingrese nota de 0 a 7:'))
    return nota

def agregar(materias):
    print(f'Las asignaturas son las siguientes:')
    number = 1
    for m in materias:
        print(f'{number}.- {m}')
        number += 1
    opcion = int(input('Seleccione materia a agregar nota:'))

    match opcion:
        case 1:
            print(f'Agregar nota a Lenguaje:')
            salir = 'n'
            while salir != 's':
                nota = masNota()
                lenguaje.append(nota)
                salir = input('Teclee "s" para salir. sino presione entre e ingrese otra nota:')
            hayNota(lenguaje)
            
        case 2:
            print(f'Agregar nota a Matemáticas:')
            salir = 'n'
            while salir != 's':
                nota = masNota()
                matematicas.append(nota)
                salir = input('Teclee "s" para salir. sino presione entre e ingrese otra nota:')
            hayNota(matematicas)

        case 3:
            print(f'Agregar nota a Historia:')
            salir = 'n'
            while salir != 's':
                nota = masNota()
                historia.append(nota)
                salir = input('Teclee "s" para salir. sino presione entre e ingrese otra nota:')
            hayNota(historia)
            
        case 4:
            print(f'Agregar nota a Ciencias:')
            salir = 'n'
            while salir != 's':
                nota = masNota()
                ciencias.append(nota)
                salir = input('Teclee "s" para salir. sino presione entre e ingrese otra nota:')
            hayNota(ciencias)
        case 5:
            print(f'Agregar nota a Música:')
            salir = 'n'
            while salir != 's':
                nota = masNota()
                musica.append(nota)
                salir = input('Teclee "s" para salir. sino presione entre e ingrese otra nota:')
            hayNota(musica)
            
        case 6:
            print(f'Agregar nota a Arte:')
            salir = 'n'
            while salir != 's':
                nota = masNota()
                arte.append(nota)
                salir = input('Teclee "s" para salir. sino presione entre e ingrese otra nota:')
            hayNota(arte)

def quitarNota(asignatura):
    while True:
        nota = int(input('Nota a quitar:'))
        print(asignatura)
        if nota in asignatura:
            print('La Nota ingresada será correctamente removida.')
            return nota
        else:
            print('La nota seleccionada no existe en el sistema. Ingrese nota existente.')

def borrar(materias):
    print(f'Las asignaturas son las siguientes:')
    number = 1
    for m in materias:
        print(f'{number}.- {m}')
        number += 1
    opcion = int(input('Seleccione materia a borrar nota:'))
    match opcion:
        case 1:
            print(f'Quitar nota a Lenguaje:')
            salir = 'n'
            asignatura = list(lenguaje)
            while salir != 's':
                nota = quitarNota(asignatura)
                lenguaje.remove(nota)
                salir = input('Teclee "s" para salir. sino presione enter para remover otra nota:')
            print('Las notas de lenguaje ahora son:')
            hayNota(lenguaje)
            
        case 2:
            print(f'Quitar nota a Matemática:')
            salir = 'n'
            asignatura = list(matematicas)
            while salir != 's':
                nota = quitarNota(asignatura)
                matematicas.remove(nota)
                salir = input('Teclee "s" para salir. sino presione enter para remover otra nota:')
            print('Las notas de matemáticas ahora son:')
            hayNota(matematicas)

        case 3:
            print(f'Quitar nota a Historia:')
            salir = 'n'
            asignatura = list(historia)
            while salir != 's':
                nota = quitarNota(asignatura)
                historia.remove(nota)
                salir = input('Teclee "s" para salir. sino presione enter para remover otra nota:')
            print('Las notas de Historia ahora son:')
            hayNota(historia)
            
        case 4:
            print(f'Quitar nota a Ciencias:')
            salir = 'n'
            asignatura = list(ciencias)
            while salir != 's':
                nota = quitarNota(asignatura)
                ciencias.remove(nota)
                salir = input('Teclee "s" para salir. sino presione enter para remover otra nota:')
            print('Las notas de Ciencias ahora son:')
            hayNota(ciencias)
        case 5:
            print(f'Quitar nota a Música:')
            salir = 'n'
            asignatura = list(lenguaje)
            while salir != 's':
                nota = quitarNota(asignatura)
                musica.remove(nota)
                salir = input('Teclee "s" para salir. sino presione enter para remover otra nota:')
            print('Las notas de Música ahora son:')
            hayNota(musica)
            
        case 6:
            print(f'Quitar nota a Arte:')
            salir = 'n'
            asignatura = list(arte)
            while salir != 's':
                nota = quitarNota(asignatura)
                arte.remove(nota)
                salir = input('Teclee "s" para salir. sino presione enter para remover otra nota:')
            print('Las notas de arte ahora son:')
            hayNota(arte)

def main(materias, asignatura):
    print('****** BIENVENIDE AL EVALUADER ******\n')
    print('*** POR FAVOR  INGRESE UNA OPCIÓN ***')
    menu = 1
    while menu != 4:
        try:
            print('1.- Ver notas.\n2.- Agregar nota.\n3.- Borrar nota.\n4.- Salir')
            menu = int(input('Opción:'))
            match menu:
                case 1:
                    ver(asignatura, materias)
                case 2:
                    agregar(materias)
                case 3:
                    borrar(materias)
                case 4:
                    print('*** SALIENDE DEL EVALUADER ***')
                case _:
                    print('MENU NO VALIDO!!!\nINGRESE MENU DEL 1 AL 4')
        except ValueError:
            print('Menú invalido. ingrese un menu correcto.')
    
if __name__ == "__main__":
    main(materias, asignatura)



