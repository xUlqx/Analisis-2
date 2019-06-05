from domicilio import Domicilio

class Persona():
    
    def __init__ (self, nombre, apellido):
        self._nombre = nombre
        self._apellido = apellido
        self._refDomicilio = []
    
    @property
    def refDomicilio(self):
        return self._refDomicilio

    @refDomicilio.setter
    def refDomicilio(self, refDomicilio):
        self._refDomicilio = refDomicilio

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @nombre.deleter
    def nombre(self):   #para borrar el valor
        del self._nombre
    
    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
    
    def agregarDomicilio(self, tipo, calle, numero):
        self._refDomicilio.append(Domicilio(tipo, calle, numero))
    
    def mostrarDomicilio(self):
        return str(''.join(str(self._refDomicilio)))