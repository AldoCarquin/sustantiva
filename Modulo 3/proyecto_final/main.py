import math
from funciones import calculadora
from funciones import contactos
# from funciones import tareas

def main():
    while True:
        menu = int(input("ingrese menu:"))
        match menu:
            # case 1:
            #     tareas
            case 2:
                contactos.main()
            case 3:
                calculadora.main()
            case _:
                print('SALIENDO DE TODO.')
                break


if __name__ == "__main__":
    main()