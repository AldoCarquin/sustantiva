contactos = {
    "tobi": 949494994,
    "aldo": 929299292,
    "Tyfany": 3141321,
    "shiuska": 3142132
}

def main():
    opcion = 0
    print(",          ,")
    print("|\\\\\  ////")
    print("| \\\\\V/// |")
    print("|  |~~~|  |")
    print("|  |===|  |")
    print("|  |   |  |      REGISTRO DE CONTACTOS")
    print("|  | ☏ |  |")
    print(" \ |   | /")
    print("  \|===|/")
    print("   '---'")

    while True:
        try:
            while opcion != 4:
                print("\n*************** MENU *****************\n")
                print("  1.- Ver Contactos.")
                print("  2.- Agregar contacto [➕👤].")
                print("  3.- Borrar contacto [➖👤].")
                print("  4.- Salir.\n")

                
                opcion = int(input("Ingrese menu:"))
                menu(opcion)

        except ValueError:
            print("Valor no valido. Ingrese un valor coherente.")


def menu(opcion):
    match opcion:
        case 1:
            ver (contactos)
        case 2:
            print("*** AGREGAR CONTACTO [➕👤] ***")
            agregar(contactos)
        case 3:
            print("*** AGREGAR CONTACTO [➖👤] ***")
            borrar(contactos)
        case 4:
            print("*** SALIENDO ***")
        case _:
            print("POR FAVOR INGRESE UN MENÚ VALIDO.")

def ver(contactos):
    if len(contactos) == 0:
        print("El directorio está vacio.")
    else:
        number = 1
        for x,y in contactos.items():
            print(f"{number}.- {x}: {y}")
            number += 1

def agregar(contactos):
    persona = input("Ingrese nombre del contacto:")
    numero = input("Ingrese número de contacto:")
    contactos[persona] = numero
    print(f"Contacto con nombre {persona} y número {numero} agregado correctamente.")

def borrar(contactos):
    if len(contactos) == 0:
        print("El directorio esstá vacío.")
    else:
        print("La lista de contactos es la siguiente:")

        count = 0
        number = 1
        for nombre,numero in contactos.items():
            print(f"{number}.- {nombre}: {numero}")
            number += 1

        eliminar = int(input("\nIngrese índice del contacto a borrar:"))-1
        for nombre,numero in contactos.items():
            if count == eliminar:
                contactos.pop(nombre)
                print(f"Contacto {nombre} con el número {numero} ha sido borrado.")
                break
            count +=1

    

if __name__ == "__main__":
    main()