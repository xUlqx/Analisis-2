
from alumno import Alumno
from profesor import Profesor

al1 = Alumno("Carlos", "Lopez", 3314)
pro1 = Profesor("Alberto", "Cortez", 5, "Licenciado")

print("Nombre:", al1.nombre)
print("Apellido:", al1.apellido)
print("Numero de legajo:", al1.legajo)

print("\nNombre:",pro1.nombre)
print("Apellido:", pro1.apellido)
print("Cantidad de hijos:", pro1.cantHijos)
print("Titulo:", pro1.titulo)