
class Domicilio():

    def __init__(self, calle, numero):
        self._calle = calle
        self._numero = numero
    
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