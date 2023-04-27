class CuentaBancaria:

    def __init__(self, numero, titular, balance):
        self.numero = numero
        self.titular = titular
        self.balance = balance

    def generar_balance(self):
        print(self.balance)

    def depositar(self, monto):
        if monto > 0:
            self.balance += monto

    