class AutoElectrico:
    def __init__(self, bateria: float):
        self.__bateria = bateria
    
    def get_bateria(self):
        return self.__bateria
    
    def set_bateria(self, energia):
        if energia > 100:
            self.__bateria = 100
        elif energia < 0:
            self.__bateria = 0
        else:
            self.__bateria = energia
    
    def cargar(self, energia: float):
        self.set_bateria(self.__bateria + energia)
    
    def conducir(self, km):
        self.set_bateria(self.__bateria - km)