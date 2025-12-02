from clases.empleado_comision import EmpleadoComision
from clases.empleado_por_hora import EmpleadoPorHora
from clases.empleado import Empleado

empleado1 = Empleado()
empleado_ph1 = EmpleadoPorHora()
empleado_com1 = EmpleadoComision()

print(empleado1.get_salario())
print(empleado_ph1.get_salario())
print(empleado_com1.get_salario())

print("\n")
print("Empleado:")
print(empleado1.set_salario(700000.0))
print(f"Pago {empleado1.calcular_pago()}")

print("\n")
print("Empleado comision:")
print(empleado_com1.set_salario(500000.0))
print(f"Pago {empleado_com1.calcular_pago()}")

print("\n")
print("Empleado por hora:")
print(empleado_ph1.set_horas(160.0))
print(f"Pago {empleado_ph1.calcular_pago()}")