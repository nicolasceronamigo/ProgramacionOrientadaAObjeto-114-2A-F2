from clase_cuenta.cuenta import CuentaBancaria

cuenta1 = CuentaBancaria(1, "Juan")

cuenta1.mostrarDatos()
cuenta1.depositar(100)
cuenta1.mostrarDatos()
cuenta1.retirar(30)
cuenta1.mostrarDatos()