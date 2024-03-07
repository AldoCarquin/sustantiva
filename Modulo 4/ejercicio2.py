
class Cuenta_bacaria:

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
        print(f'El saldo en la cuenta de {self.titular} es de ${self.monto} euros')

cuenta1 = Cuenta_bacaria('123456789', 'Juan Perez', 1000)
cuenta2 = Cuenta_bacaria('987654321', 'María Lopez', 500)


cuenta1.mostrar_saldo()
cuenta1.depositar(500)
cuenta1.mostrar_saldo()
print('********************')
cuenta2.mostrar_saldo()
cuenta2.girar(200)
cuenta2.mostrar_saldo()
print('********************')
cuenta1.mostrar_saldo()
cuenta2.mostrar_saldo()