from datetime import datetime

class Autor:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Libro:
    def __init__(self, titulo, autor, ejemplares):
        self.titulo = titulo
        self.autor = autor
        self.ejemplares = ejemplares

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                return libro
        return None

    def listar_libros(self):
        print("Libros en la biblioteca:")
        for libro in self.libros:
            print(f"- {libro.titulo} de {libro.autor.nombre} {libro.autor.apellido} ({libro.ejemplares} ejemplares)")

    def ingresar_libro(self):
        titulo = input("Ingrese el título del libro: ")
        autor_nombre = input("Ingrese el nombre del autor: ")
        autor_apellido = input("Ingrese el apellido del autor: ")
        ejemplares = int(input("Ingrese la cantidad de ejemplares disponibles: "))

        autor = Autor(autor_nombre, autor_apellido)
        libro = Libro(titulo, autor, ejemplares)
        self.agregar_libro(libro)
        print("¡Libro ingresado con éxito!")

class Préstamo:
    def __init__(self, libro, fecha_inicio):
        self.libro = libro
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = None

    def devolver_libro(self, fecha_devolucion):
        self.fecha_fin = fecha_devolucion

def pedir_prestamo(biblioteca):
    titulo = input("Ingrese el título del libro que desea pedir prestado: ")
    libro = biblioteca.buscar_libro(titulo)
    if libro:
        if libro.ejemplares > 0:
            fecha_inicio = datetime.now()
            prestamo = Préstamo(libro, fecha_inicio)
            print("¡Préstamo realizado con éxito!")
            print(f"Fecha de inicio del préstamo: {fecha_inicio}")
        else:
            print("Lo siento, no quedan ejemplares disponibles de este libro.")
    else:
        print("Libro no encontrado en la biblioteca.")

def main():
    # Crear biblioteca
    biblioteca = Biblioteca()

    while True:
        print('*** BIENVENIDO A LA BIBLIOTECA ***')
        print("\nMENU:")
        print("1. Listar libros disponibles")
        print("2. Pedir prestamo de un libro")
        print("3. Ingresar un nuevo libro")
        print("4. Salir")

        opcion = input("Ingrese el número de la opción que desea realizar: ")

        if opcion == "1":
            biblioteca.listar_libros()
        elif opcion == "2":
            pedir_prestamo(biblioteca)
        elif opcion == "3":
            biblioteca.ingresar_libro()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()
