import math
from funciones import calculadora
from funciones import contactos
from funciones import listaTareas
from funciones import evaluador
from funciones.listaTareas import tareas
from funciones.listaTareas import tareasRealizadas
from funciones.evaluador import materias
from funciones.evaluador import asignatura

def main(tareas, tareasRealizadas, materias, asignatura):
    while True:
        menu = int(input("ingrese menu:\n1.- Tareas a realizas.\n2.- Registro de contactos.\n3.- Calculadora avanzada.\n4.- Evaluader de materies.\n5.- Salir\nOpcion:"))
        match menu:
            case 1:
                listaTareas.main(tareas, tareasRealizadas)
            case 2:
                contactos.main()
            case 3:
                calculadora.main()
            case 4:
                evaluador.main(materias, asignatura)
            case 5:
                print('SALIENDO DE TODO.')
                break
            case _:
                print('VALOR INVALIDO.')


if __name__ == "__main__":
    main(tareas, tareasRealizadas, materias, asignatura)