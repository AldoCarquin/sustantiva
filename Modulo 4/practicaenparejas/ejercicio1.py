class Auto():

    def __init__(self, color, marca, modelo, numeroPuertas, patente):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.numeroPuertas = numeroPuertas
        self.patente = patente

    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color

    def get_marca(self):
        return self.marca
    
    def set_marca(self, marca):
        self.marca = marca

    def get_modelo(self):
        return self.modelo
    
    def set_modelo(self, modelo):
        self.modelo = modelo

    def get_numeroPuertas(self):
        return self.numeroPuertas
    
    def set_numeroPuertas(self, numeroPuertas):
        self.numeroPuertas = numeroPuertas

    def get_patente(self):
        return self.patente
    
    def set_patente(self, patente):
        self.patente = patente

    def ingreso_auto():
        global number
        print(f'Auto número {number}')
        color = input(f'Ingrese el color del auto {number}: ')
        marca = input(f'Ingrese la marca del auto {number}: ')
        modelo = input(f'Ingrese el modelo del auto {number}: ')
        numero_puertas = input(f'Ingrese el número de puertas del auto {number}: ')
        patente = input(f'Ingrese la patente del auto {number}: ')

        nuevo_auto = Auto(color, marca, modelo, numero_puertas, patente)
        autos.append(nuevo_auto)
    
    def ver_autos():
        print(f'AUTOS INGRESADOS {number}')
        print('')
        for idx, Auto in enumerate(autos, start=1):
            print(f'** AUTO NUMERO {idx} **')
            print(f'Auto de color {Auto.get_color()}, marca {Auto.get_marca()} modelo {Auto.get_modelo()} con {Auto.get_numeroPuertas()} puertas y patente {Auto.get_patente()}.')

            print()


autos = []
number = 0

def main():
    print('\n*** BIENVENIDO AL INDEXADOR DE AUTOS ***\n')
    while True :
        print('Por favor ingrese un menu:')
        print('1.- Ingresar vehículo')
        print('2.- Ver vehiculos')
        print('3.- Salir\n')
        menu = int(input('Ingrese una opción: '))
        print('')

        match menu:
            case 1:
                while True:
                    global number
                    number += 1
                    Auto.ingreso_auto()
                    continuar = input("¿Desea ingresar otro coche? (s/n): ")
                    if continuar.lower() != 's':
                        break
            case 2:
                Auto.ver_autos()
            case 3:
                if number >= 5:
                    print('*** GRACIAS POR USAR EL INDEXADOR DE AUTOS ***')
                    break
                else:
                    faltantes = 5-number
                    print(f'No puede salir del programa con menos de 5 vehículos.\nPor favor ingrese {faltantes} más.\n')
            case _:
                print('VALOR INVALIDO. REITERE.')




if __name__ == "__main__":
    main()