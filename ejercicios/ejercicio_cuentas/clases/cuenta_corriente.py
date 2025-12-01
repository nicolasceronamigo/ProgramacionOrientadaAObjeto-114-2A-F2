from clases.cuenta_bancaria import CuentaBancaria

sobregiro = - 500

class CuentaCorriente(CuentaBancaria):
    def retirar_monto(self, monto):
        saldo_final = self.mostrar_saldo() - monto
        if monto <= 0:
            raise Exception("El monto a retirar debe ser mayor que cero")
        elif saldo_final >= 0:
            super().retirar_monto(monto)
        elif saldo_final < 0:
            if saldo_final < sobregiro:
                raise Exception("Límite de sobregiro alcanzado")
            super().set_saldo(saldo_final)