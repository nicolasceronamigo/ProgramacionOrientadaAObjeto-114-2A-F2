from clase_cuenta.cuenta import CuentaBancaria

cuenta1 = CuentaBancaria(1, "Juan")

print(cuenta1.mostrarDatos())
cuenta1.depositar(100)
print(cuenta1.mostrarDatos())
cuenta1.retirar(30)
print(cuenta1.mostrarDatos())
cuenta1.retirar(200)
print(cuenta1.mostrarDatos())