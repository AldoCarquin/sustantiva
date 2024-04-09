class Pelicula():

    def __init__(self, titulo, director, genero, duracion):
        self.titulo = titulo
        self.director = director
        self.genero = genero
        self.duracion = duracion

    def get_titulo(self):
        return self.titulo
    
    def set_titulo(self, titulo):
        self.titulo = titulo

    def get_director(self):
        return self.director
    
    def set_director(self, director):
        self.director = director

    def get_genero(self):
        return self.genero
    
    def set_genero(self, genero):
        self.genero = genero

    def get_duracion(self):
        return self.duracion
    
    def set_duracion(self, duracion):
        self.duracion = duracion

    def ingreso_Pelicula():
        global number
        print(f'Pelicula número {number}')
        titulo = input(f'Ingrese el titulo del Película {number}: ')
        director = input(f'Ingrese la director del Película {number}: ')
        genero = input(f'Ingrese el genero del Película {number}: ')
        duracion = input(f'Ingrese la duración de la película {number} (minutos): ')

        nueva_Pelicula = Pelicula(titulo, director, genero, duracion)
        Peliculas.append(nueva_Pelicula)
    
    def ver_Peliculas():
        print(f'PELICULAS INGRESADAS: {number}')
        print('')
        for idx, Pelicula in enumerate(Peliculas, start=1):
            print(f'** PELÍCULA NUMERO {idx} **')
            print(f'Pelicula de titulo {Pelicula.get_titulo()}, director {Pelicula.get_director()}, género {Pelicula.get_genero()} con {Pelicula.get_duracion()} minutos de duración.')

            print()


Peliculas = []
number = 0

def main():
    print('\n*** BIENVENIDO AL INDEXADOR DE PELÍCULAS ***\n')
    while True :
        print('Por favor ingrese un menu:')
        print('1.- Ingresar pelícuka')
        print('2.- Ver películas ingresadas')
        print('3.- Salir\n')
        menu = int(input('Ingrese una opción: '))
        print('')

        match menu:
            case 1:
                while True:
                    global number
                    number += 1
                    Pelicula.ingreso_Pelicula()
                    continuar = input("¿Desea ingresar otra película? (s/n): ")
                    if continuar.lower() != 's':
                        break
            case 2:
                Pelicula.ver_Peliculas()
            case 3:
                if number >= 5:
                    print('*** GRACIAS POR USAR EL INDEXADOR DE PeliculaS ***')
                    break
                else:
                    faltantes = 5-number
                    print(f'No puede salir del programa con menos de 5 vehículos.\nPor favor ingrese {faltantes} más.\n')
            case _:
                print('VALOR INVALIDO. REITERE.')




if __name__ == "__main__":
    main()