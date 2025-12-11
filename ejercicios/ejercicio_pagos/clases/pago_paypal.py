from clases.pago import Pago

class PagoPaypal(Pago):
    def procesar_pago(self, monto):
        return f"Pago de {monto} procesado con PayPal"