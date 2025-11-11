import re

class Persona:
    def __init__(self, nombre, apellido, telefono, correo_elec):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__telefono = telefono
        self.__correo_elec = correo_elec
    
    def get_nombre(self):
        return self.__nombre
    
    @property
    def correo_elec(self):
        return self.__correo_elec
    
    @correo_elec.setter
    def set_correo_elec(self, nuevo_correo):
        patron_correo = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        valido = re.match(patron_correo, nuevo_correo)
        if valido:
            self.__correo_elec = nuevo_correo
            return True
        return False