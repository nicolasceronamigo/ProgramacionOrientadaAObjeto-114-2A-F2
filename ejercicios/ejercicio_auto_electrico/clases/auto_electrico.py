class AutoElectrico:
    def __init__(self, bateria: float):
        self.__bateria = bateria
    
    def get_bateria(self):
        return self.__bateria
    
    def set_bateria(self, energia: float):
        conduccion = self.__bateria - energia
        carga = energia - self.__bateria
        if energia > 100:
            excepcion = f"No se puede cargar {carga}% de energía. Se supera la capacidad de la batería.\n Carga actual: {self.__bateria}%."
            return excepcion
        elif energia < 0:
            excepcion = f"No hay suficiente bateria para conducir {conduccion} km.\n Carga actual: {self.__bateria}%."
            return excepcion
        else:
            if energia > self.__bateria: #está cargando 
                self.__bateria = energia
                return f"Se cargó {carga}%. Carga actual: {self.__bateria}%"
            elif energia < self.__bateria: #está conduciendo
                self.__bateria = energia
                return f"Se condujo {conduccion} km. Carga actual: {self.__bateria}%"
            return f"No se efectuó ningún cambio. Carga actual: {self.__bateria}%"
            
    
    def cargar(self, energia: float):
        return self.set_bateria(self.__bateria + energia)
    
    def conducir(self, km: float):
        return self.set_bateria(self.__bateria - km)