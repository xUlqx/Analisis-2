from persona import Persona
from domicilio import Domicilio

per1 = Persona("Carlos", "Lopez", "9 de Julio", 555)

print("Nombre:", per1.nombre)
print("Apellido:", per1.apellido)
print("Calle:", per1.refDomicilio.calle)
print("Número de calle:" ,per1.refDomicilio.numero)

#Cambiamos el nombre de la calle y el numero
per1.refDomicilio.calle = "España"
per1.refDomicilio.numero = 987

print("\nNombre:", per1.nombre)
print("Apellido:", per1.apellido)
print("Calle:", per1.refDomicilio.calle)
print("Número de calle:" ,per1.refDomicilio.numero)