from clases.empleado import Empleado

tarifa = 10000

class EmpleadoPorHora(Empleado):
    def __init__(self):
        super().__init__() #usa el atributo __salario de la clase padre
        self.__horas = 0.0
    
    def set_horas(self, horas: float):
        if horas > 0:
            self.__horas = horas
            return f"Horas: {horas}"
        return "Horas deben ser mayor que 0"
    
    def get_horas(self):
        return self.__horas
    
    def calcular_pago(self):
        return tarifa * self.get_horas()