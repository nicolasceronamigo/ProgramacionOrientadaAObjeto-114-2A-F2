from clases.pago import Pago

class PagoTarjeta(Pago):
    def procesar_pago(self, monto):
        return f"Pago de {monto} procesado con tarjeta"