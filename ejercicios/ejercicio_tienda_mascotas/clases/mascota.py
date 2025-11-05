class Mascota:
    def __init__(self, nombre:str , especie:str , edad: int):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
    def mostrar_datos(self) -> str:
        return f"| Nombre: {self.nombre} | Especie: {self.especie} | Edad: {self.edad} |"