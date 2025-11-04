# Crea una clase llamada CuentaBancaria que represente una
# cuenta simple.

# Campos de clase:
# numeroCuenta
# titular
# saldo.

# Métodos:
# Un constructor que reciba numeroCuenta, titular y un
# saldo inicial.
# Un método depositar(monto) que sume el monto al saldo.
# Un método retirar(monto) que reste el monto al saldo
# solo si hay saldo suficiente.
# Un método mostrarDatos() que imprima algo como:
# "Cuenta: [numeroCuenta] - Titular: [titular] - Saldo:
# [saldo]".

class CuentaBancaria:
    def __init__(self, numeroCuenta: int, titular: str, saldo:float = 0.0):
        self.numeroCuenta = numeroCuenta
        self.titular = titular
        self.saldo = saldo
    def depositar(self, monto: float):
        self.saldo += monto
    def retirar(self, monto: float):
        if self.saldo < monto:
            raise Exception("Saldo insuficiente")
        self.saldo -= monto
    def mostrarDatos(self):
        return f"Cuenta: {self.numeroCuenta} - Titular: {self.titular}, Saldo: {self.saldo}"

