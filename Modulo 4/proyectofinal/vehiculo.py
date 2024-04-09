class Vehiculo:
    def __init__(self, marca, modelo, color, velocidad):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = velocidad

    def acelerar(self):
        self.velocidad += 10

    def frenar(self):
        self.velocidad -= 5

    def imprimir_estado(self):
        print("Estado del vehículo:")
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Color:", self.color)
        print("Velocidad:", self.velocidad, "km/h")
        print()

def mostrar_menu():
    print("Menu:")
    print("1. Acelerar")
    print("2. Frenar")
    print("3. Salir")

def main():

    
    vehiculo = Vehiculo("Toyota", "Corolla", "Rojo", 0)

    # Loop del menú
    while True:
        vehiculo.imprimir_estado()
        mostrar_menu()
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            vehiculo.acelerar()
        elif opcion == "2":
            vehiculo.frenar()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
