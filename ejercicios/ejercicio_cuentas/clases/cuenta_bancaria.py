
class CuentaBancaria:
    def __init__(self):
        self.__saldo = 0
    
    def depositar_monto(self, monto: int):
        if monto < 0:
            raise Exception("El monto a depositar debe ser mayor o igual que cero")
        self.__saldo += monto
    
    def retirar_monto(self, monto: int):
        if monto < 0:
            raise Exception("El monto a retirar debe ser mayor o igual que cero")
        if self.__saldo < monto:
            raise Exception("Saldo insuficiente")
        self.__saldo -= monto
    
    def mostrar_saldo(self):
        return self.__saldo
    
    def set_saldo(self, monto):
        self.__saldo = monto