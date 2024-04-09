menu = 0
number = 0
estudiantes = []

class Estudiante:

    def __init__(self, nombre, edad, notas):
        self.nombre = nombre
        self.edad = edad
        self.notas = notas

    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_edad(self):
        return self.edad
    
    def set_edad(self, edad):
        self.edad = edad

    def get_notas(self):
        return self.notas
    
    def set_notas(self, notas):
        self.notas = notas

    @staticmethod
    def ing_nuevo_estudiante():
        global number
        number += 1
        print(f'Estudiante nº{number}')
        nombre = input(f'Ingrese el nombre del estudiante nº{number}: ')
        edad = ing_edad()
        notas = ing_notas()
        nuevo_alumno = Estudiante(nombre, edad, notas)
        estudiantes.append(nuevo_alumno)
        suma = sum(notas)
        total = len(notas)
        promedio = suma/total
        print(f'Se ha ingresado al estudiante nº{number} con nombre {nombre} y un promedio de {promedio} correctamente.')
    
    def imprimir(self):
        suma = sum(self.notas)
        total = len(self.notas)
        promedio = suma/total
        print (f'Nombre: {self.nombre} | Edad: {self.edad} | Notas: {self.notas} | Promedio: {promedio}')

def in_menu():
    print('1.- Ingresar nuevo alumno')
    print('2.- Ver alumno')
    print('3.- Salir ')

    opcion = int(input('\nIngrese una opción: '))
    return opcion

def ing_edad():
    while True:
        try:
            edad = int(input("Ingrese la edad: "))
            return edad
        except ValueError:
            print("Error: Debe ingresar un valor numérico.") 

def ing_notas():
    calificaciones = []
    print('Ingrese notas y presione enter. Si no quiere ingresar más notas, presione n.')
    contador = 1
    while True:
        entrada = input(f'Nota {contador}: ')
        if entrada.lower() == 'n':
            break
        try:
            nota = int(entrada)
            calificaciones.append(nota)
            contador += 1
        except ValueError:
            print('Debe ingresar un número entero válido.')
    return calificaciones

def ver_alumno():
    cuantos = len(estudiantes)
    if cuantos == 0:
        print('No hay estudiantes para mostrar. Por favor ingrese uno\n')
    else:
        print(f'Existen {cuantos} estudiantes ingresados\n')
        for estudiante in estudiantes:
            estudiante.imprimir()
            print('')

def main():
    global menu
    print('*** BIENVENIDX AL SISTEMA DE GESTIÓN DE ESTUDIANTES ***.')
    print('Por favor, seleccione una opción:\n')

    while True:
        try:

            menu = in_menu()
            if menu == 1:
                Estudiante.ing_nuevo_estudiante()
            elif menu == 2:
                ver_alumno()
            elif menu == 3:
                print('Gracias. Hasta pronto.')
                break
        except ValueError:
            print('Ingrese menu valido')

if __name__ == "__main__":
    main()
