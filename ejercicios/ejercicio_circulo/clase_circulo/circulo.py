# Crea una clase llamada Circulo que tenga:
# Un constructor que reciba el radio como parámetro.
# Un método llamado área que calcule y devuelva el área
# del círculo (usa la fórmula: área = π * radio^2).

# Instrucciones:
# Crea una instancia de Circulo con radio 5.
# Llama al método área e imprime el resultado.

import math

class Circulo:
    def __init__(self, radio: float):
        self.radio = radio
    def area(self) -> float:
        calculo_area = math.pi * math.pow(self.radio, 2)
        return calculo_area