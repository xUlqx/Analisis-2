
from persona import Persona
from domicilio import Domicilio

per1 = Persona("Carlos", "Lopez")
dom1 = Domicilio("9 de Julio", 555)
per1.refDomicilio = dom1

print("Nombre:", per1.nombre)
print("Apellido:", per1.apellido)
print("Calle:", per1.refDomicilio.calle)
print("Número de calle:" ,per1.refDomicilio.numero)