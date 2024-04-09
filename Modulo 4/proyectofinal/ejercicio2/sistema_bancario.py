import random

cuentas_bancarias = []

class CuentaBancaria:

    def __init__(self, cuenta, titular, monto):
        self.cuenta = cuenta
        self.titular = titular
        self.monto = monto

    # GETTERS AND SETTERS

    def get_cuenta(self):
        return self.cuenta
    
    def set_cuenta(self, cuenta):
        self.cuenta = cuenta

    def get_titular(self):
        return self.titular
    
    def set_titular(self, titular):
        self.titular = titular

    def get_monto(self):
        return self.monto
    
    def set_monto(self, monto):
        self.monto = monto

    # METODOS

    def depositar(self, depositar):
        self.monto += depositar

    def girar(self, sacar):
        self.monto -= sacar
    
    def mostrar_saldo(self):
        print(f'La cuenta número {self.cuenta} de {self.titular} es de ${self.monto} euros')

def nueva_cuenta():
    titular = input('\nIngrese nombre del titular de la cuenta: ')
    cuenta = random.randint(100000, 999999)
    while True:
        try:
            monto = int(input('Ingrese monto de apertura de cuenta: $'))
            break
        except ValueError:
            print('Ingrese sólo números')
    nueva_cuenta = CuentaBancaria(cuenta, titular, monto)
    cuentas_bancarias.append(nueva_cuenta)
    print('')

def ver_cuentas():
    cuantas = len(cuentas_bancarias)
    if cuantas == 0:
        print('No hay cuentas bancarias ingresadas. Por favor cree alguna.')
    else:
        print(f'Existen {cuantas} cuentas bancarias')
        for n in cuentas_bancarias:
            n.mostrar_saldo()
            print('')

def depositar_dinero():
    ver_cuentas()
    cuenta_numero = int(input("Ingrese el número de cuenta en el que desea depositar dinero: "))
    cuenta = None
    for c in cuentas_bancarias:
        if c.get_cuenta() == cuenta_numero:
            cuenta = c
            break
    if cuenta is None:
        print("Número de cuenta inválido.")
        return
    monto_deposito = int(input("Ingrese la cantidad que desea depositar: "))
    cuenta.depositar(monto_deposito)
    print("¡Depósito exitoso!")

def retirar_dinero():
    ver_cuentas()
    cuenta_numero = int(input("Ingrese el número de cuenta de la que desea retirar dinero: "))
    cuenta = None
    for c in cuentas_bancarias:
        if c.get_cuenta() == cuenta_numero:
            cuenta = c
            break
    if cuenta is None:
        print("Número de cuenta inválido.")
        return
    monto_retiro = int(input("Ingrese la cantidad que desea retirar: "))
    if monto_retiro <= cuenta.get_monto():
        cuenta.girar(monto_retiro)
        print("¡Retiro exitoso!")
    else:
        print("Fondos insuficientes.")

def in_menu():
    print('1.- Ingresar nueva cuenta')
    print('2.- Ver cuentas')
    print('3.- Depositar dinero')
    print('4.- Retirar dinero')
    print('5.- Salir')

    opcion = int(input('\nIngrese una opción: '))
    return opcion

def main():
    global menu
    print('*** BIENVENIDX AL BANCO POTAXIE ***.')
    print('Por favor, seleccione una opción:\n')

    while True:
        try:
            menu = in_menu()
            if menu == 1:
                nueva_cuenta()
            elif menu == 2:
                ver_cuentas()
            elif menu == 3:
                depositar_dinero()
            elif menu == 4:
                retirar_dinero()
            elif menu == 5:
                print('Gracias. Hasta pronto.')
                break
        except ValueError:
            print('Ingrese menu valido')

if __name__ == "__main__":
    main()
