
class Domicilio():

    def __init__(self, tipo, calle, numero):
        self._tipo = tipo
        self._calle = calle
        self._numero = numero
    
    @property
    def tipo (self):
        return self._tipo
    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @property
    def calle(self):
        return self._calle
    @calle.setter
    def calle(self, calle):
        self._calle = calle
    
    @property
    def numero(self):
        return self._numero
    @numero.setter
    def numero(self, numero):
        self._numero = numero

    def __repr__(self):
        return '\n  Tipo de domicilio: {}\n  Calle: {}\n  Numero: {}\n\n'.format(
            self._tipo,
            self._calle, 
            self._numero,
        )

