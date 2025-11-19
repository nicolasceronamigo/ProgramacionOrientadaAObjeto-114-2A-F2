from clases.comprobante import Comprobante

class Factura(Comprobante):
    def __init__(self, id, fecha, monto, rut_cliente):
        super().__init__(id, fecha, monto)
        self.__rut_cliente = rut_cliente
    
    @property
    def get_rut_cliente(self):
        return self.__rut_cliente
    
    @get_rut_cliente.setter
    def set_rut_cliente(self, rut_cliente):
        self.__rut_cliente = rut_cliente
    
    def resumen_factura(self):
        resumen = f"Factura ID: {self.get_id} | Fecha: {self.get_fecha} | Monto: ${self.get_monto} | Cliente: {self.get_rut_cliente}"
        return resumen