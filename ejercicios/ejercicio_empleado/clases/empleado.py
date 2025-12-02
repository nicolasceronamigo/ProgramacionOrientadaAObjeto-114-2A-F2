
class Empleado:
    def __init__(self):
        self.__salario = 0
    
    def set_salario(self, salario: int):
        if salario > 0:
            self.__salario = salario
            return f"Salario: {salario}"
        return "El salario debe ser mayor que 0"
    
    def get_salario(self):
        return f"Salario: {self.__salario}"
    
    def calcular_pago(self):
        return self.__salario