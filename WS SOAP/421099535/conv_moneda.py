from spyne import Application, rpc, ServiceBase, Integer, Float, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class CurrencyConverterService(ServiceBase):
    @rpc(Float, Unicode, Unicode, _returns=Float)
    def convert(ctx, amount, from_currency, to_currency):
        # Ejemplo simple, en la práctica se usaría una API externa para obtener las tasas de cambio
        rates = {'USD': 1.0, 'EUR': 0.85, 'MXN': 20.0}
        return amount * rates[to_currency] / rates[from_currency]

application = Application(
    [CurrencyConverterService],
    tns='spyne.examples.currency_converter',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11())

wsgi_app = WsgiApplication(application)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('127.0.0.1', 8000, wsgi_app)
    print("Serving on port 8000...")
    server.serve_forever()