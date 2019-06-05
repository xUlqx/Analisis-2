from persona import Persona
from domicilio import Domicilio


per1 = Persona("Robert", "Johnson")
per1.agregarDomicilio('Casa', '9 de Julio', 1555)
per1.agregarDomicilio('Comercial', 'Patricia', 2777)

print("Nombre:", per1.nombre)
print("Apellido:", per1.apellido)
print("Los domicilios de la persona son: \n", per1.mostrarDomicilio())