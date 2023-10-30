
class Servicios:

    def __init__(self, id, servicios, tipo, USD ) -> None:
        self.id = id
        self.servicios = servicios
        self.tipo = tipo
        self.USD = USD


    def serialize(self):
        return {
            'id': self.id,
            'Servicios': self.servicios,
            'Tipo': self.tipo,
            'USD': self.USD
        }

    def serialize_arg(self):
        return {
            'servicios': self.servicios,
            'USD': self.USD
        }