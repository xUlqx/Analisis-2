from persona import Persona

class Alumno(Persona):
    def __init__(self, nombre, apellido, legajo):
        super().__init__(nombre, apellido)
        self._legajo = legajo
        
    @property
    def legajo(self):
        return self._legajo
    @legajo.setter
    def legajo(self, legajo):
        self._legajo = legajo