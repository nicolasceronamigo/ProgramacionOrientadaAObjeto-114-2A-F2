from clases.cuenta_bancaria import CuentaBancaria
from clases.cuenta_ahorro import CuentaAhorro
from clases.cuenta_corriente import CuentaCorriente

cuentaB = CuentaBancaria()
cuentaB.depositar_monto(100)
cuentaB.retirar_monto(60)

cuentaA = CuentaAhorro()
cuentaA.depositar_monto(100)
cuentaA.retirar_monto(60)

cuentaC = CuentaCorriente()
cuentaC.depositar_monto(100)
cuentaC.retirar_monto(300)

cuentas = [cuentaB, cuentaA, cuentaC]

for cuenta in cuentas:
    print(cuenta.mostrar_saldo())
