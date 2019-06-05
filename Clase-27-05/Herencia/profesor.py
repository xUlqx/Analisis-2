from persona import Persona

class Profesor(Persona):
    def __init__(self, nombre, apellido, cantHijos, titulo):
        super().__init__(nombre, apellido)
        self._cantHijos = cantHijos
        self._titulo = titulo
    
    @property
    def cantHijos(self):
        return self._cantHijos
    @cantHijos.setter
    def cantHijos(self, cantHijos):
        self._cantHijos = cantHijos

    @property
    def titulo(self):
        return self._titulo
    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo