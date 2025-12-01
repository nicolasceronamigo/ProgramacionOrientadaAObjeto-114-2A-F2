from clases.cuenta_bancaria import CuentaBancaria

interes = 0.02

class CuentaAhorro(CuentaBancaria):
    def mostrar_saldo(self):
        self.depositar_monto(super().mostrar_saldo() * interes)
        return super().mostrar_saldo()