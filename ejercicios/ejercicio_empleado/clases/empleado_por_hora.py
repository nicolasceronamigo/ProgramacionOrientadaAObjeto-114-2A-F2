from clases.empleado import Empleado
cosa = 4
class EmpleadoPorHora(Empleado):
    def __init__(self):
        super().__init__() #usa el atributo __salario de la clase padre
        self.__tarifa = 0
        self.__horas = 0
    
    def set_tarifa(self, tarifa: int):
        if tarifa > 0:
            self.__tarifa = tarifa
            return f"Tarifa: {tarifa}"
        return "Tarifa debe ser mayor que 0"
    
    def get_tarifa(self):
        return self.__tarifa
    
    def set_horas(self, horas: int):
        if horas > 0:
            self.__horas = horas
            return f"Horas: {horas}"
        return "Horas deben ser mayor que 0"
    
    def get_horas(self):
        return self.__horas
    
    def calcular_pago(self):
        return self.get_tarifa() * self.get_horas()
    
    def set_salario(self):
        return super().set_salario(self.calcular_pago())