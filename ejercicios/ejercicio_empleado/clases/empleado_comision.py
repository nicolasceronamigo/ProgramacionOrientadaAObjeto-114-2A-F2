from clases.empleado import Empleado

comision = 1.1

class EmpleadoComision(Empleado):
    def calcular_pago(self):
        return self.get_salario() * comision