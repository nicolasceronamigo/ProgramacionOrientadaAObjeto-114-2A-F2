from clases.empleado import Empleado

class EmpleadoComision(Empleado):
    def __init__(self):
        super().__init__()
        self.__comision = 0
    
    def set_comision(self, comision):
        if comision > 0:
            self.__comision = comision
            return f"Comisión: {comision}"
        return "Comisión debe ser mayor que 0"
    
    def get_comision(self):
        return self.__comision
    
    def calcular_pago(self):
        return self.get_salario() + self.get_comision()
    
    def set_salario(self):
        return super().set_salario(self.calcular_pago())