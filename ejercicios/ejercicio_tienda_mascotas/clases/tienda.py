from .mascota import Mascota

class Tienda:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.lista_mascotas = []
    
    def registrar_mascota(self, mascota: Mascota):
        self.lista_mascotas.append(mascota)
    
    def consultar_listado(self):
        print(f"Listado {self.nombre}:")
        for mascota in self.lista_mascotas:
            print(mascota.mostrar_datos())
    
    def buscar_mascota(self, nombre_mascota: str):
        for mascota in self.lista_mascotas:
            if mascota.nombre == nombre_mascota:
                return mascota.mostrar_datos()
        return f"Mascota: {nombre_mascota} no está registrada en {self.nombre}"
    
    def calcular_edad_promedio_mascotas(self):
        suma_edad = 0
        if len(self.lista_mascotas) == 0:
            return f"No hay mascotas registradas en {self.nombre}, no es posible realizar el cálculo"
        for mascota in self.lista_mascotas:
            suma_edad += mascota.edad
        promedio_edad = suma_edad / len(self.lista_mascotas)
        return promedio_edad
    
    def ver_estado_registro(self, ver_promedio: bool = False):
        total_mascotas = len(self.lista_mascotas)
        if ver_promedio:
            edad_promedio = self.calcular_edad_promedio_mascotas()
            return f"Estado {self.nombre} | Total mascotas : {total_mascotas} | Edad promedio: {edad_promedio} |"
        return f"Estado {self.nombre} | Total mascotas : {total_mascotas} |"