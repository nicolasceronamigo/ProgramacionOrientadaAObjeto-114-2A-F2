#from datetime import date

class Documento:
    def __init__(self, id, fecha):
        self.__id = id
        self.__fecha = fecha
    
    @property
    def get_id(self):
        return self.__id
    
    @get_id.setter
    def set_id(self, id):
        if id < 0:
            raise Exception("El id debe ser mayor a cero")
        self.__id = id
    
    @property
    def get_fecha(self):
        return self.__fecha
    
    @get_fecha.setter
    def set_fecha(self, fecha):
        if fecha == "":
            raise Exception("La fecha no puede estar vacía")
        self.__fecha = fecha