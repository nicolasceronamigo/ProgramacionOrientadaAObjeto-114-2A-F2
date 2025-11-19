from clases.documento import Documento

class Comprobante(Documento):
    def __init__(self, id, fecha, monto):
        super().__init__(id, fecha)
        self.__monto = monto
    
    @property
    def get_monto(self):
        return self.__monto
    
    @get_monto.setter
    def set_monto(self, monto):
        if monto < 0:
            raise Exception("El monto no puede ser menor que cero")
        self.__monto = monto