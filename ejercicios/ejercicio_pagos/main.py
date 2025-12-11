from clases.pago import Pago
from clases.pago_efectivo import PagoEfectivo
from clases.pago_paypal import PagoPaypal
from clases.pago_tarjeta import PagoTarjeta

pagos = [PagoTarjeta(), PagoPaypal(), PagoEfectivo()]

for pago in pagos:
    print(pago.procesar_pago(100))