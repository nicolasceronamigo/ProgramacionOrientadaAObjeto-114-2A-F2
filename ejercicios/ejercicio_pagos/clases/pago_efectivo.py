from clases.pago import Pago

class PagoEfectivo(Pago):
    def procesar_pago(self, monto):
        return f"Pago de {monto} procesado con efectivo"